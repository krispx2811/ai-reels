"""tts.py: ElevenLabs voiceover for the video. Standard library only, plus ffmpeg.

The key is read from ELEVENLABS_API_KEY in the environment or from ../.env. It is never printed.

usage:
  python tts.py check                 is a key set? (yes/no only)
  python tts.py voices [search]       list voices on the account (name, id, language labels)
  python tts.py lines                 make one mp3 per line in vo.json, print each length vs its slot
  python tts.py mix ../out/draft.mp4 ../out/draft-vo.mp4   lay the lines on the video at their times
"""
import json, os, subprocess, sys, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
API = 'https://api.elevenlabs.io'


def key():
    k = os.environ.get('ELEVENLABS_API_KEY')
    p = os.path.join(HERE, '..', '.env')
    if not k and os.path.exists(p):
        for line in open(p, encoding='utf-8'):
            if line.strip().startswith('ELEVENLABS_API_KEY='):
                k = line.split('=', 1)[1].strip().strip('"').strip("'")
    return k or None


def call(method, path, body=None, raw=False):
    k = key()
    if not k:
        sys.exit('No key. Put ELEVENLABS_API_KEY=... in the .env file next to the proj folder.')
    req = urllib.request.Request(API + path, method=method, data=json.dumps(body).encode() if body else None,
                                 headers={'xi-api-key': k, 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = r.read()
            return data if raw else json.loads(data)
    except urllib.error.HTTPError as e:
        sys.exit(f'ElevenLabs said {e.code}: {e.read().decode(errors="replace")[:400]}')


def dur(path):
    out = subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path])
    return float(out.strip())


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'check'
    cfg = json.load(open(os.path.join(HERE, 'vo.json'), encoding='utf-8'))
    if cmd == 'check':
        print('key: yes (hidden)' if key() else 'key: no')
    elif cmd == 'voices':
        q = sys.argv[2].lower() if len(sys.argv) > 2 else ''
        r = call('GET', '/v2/voices?page_size=100' + (f'&search={urllib.parse.quote(q)}' if q else ''))
        for v in r.get('voices', []):
            labels = v.get('labels') or {}
            print(f"{v['voice_id']}  {v['name'][:40]:40}  {labels.get('language', '')} {labels.get('accent', '')} {labels.get('gender', '')}")
    elif cmd == 'lines':
        voices = cfg.get('voices') or {}
        def voice_for(ln):
            return voices.get(ln.get('speaker', ''), '') or cfg.get('voice_id', '')
        missing = [ln['id'] for ln in cfg['lines'] if not voice_for(ln)]
        if missing:
            sys.exit('Set a voice id in vo.json "voices" (or "voice_id") for: ' + ', '.join(missing))
        os.makedirs(os.path.join(HERE, 'lines'), exist_ok=True)
        only = sys.argv[2:]                      # optional: regenerate only these line ids
        lines = cfg['lines']
        for k, ln in enumerate(lines):
            if only and ln['id'] not in only:
                continue
            out = os.path.join(HERE, 'lines', ln['id'] + '.mp3')
            body = {'text': ln['text'], 'model_id': cfg['model_id'], 'language_code': cfg.get('language_code', 'ar'),
                    'apply_text_normalization': 'on'}
            # eleven_v4: only stability + similarity_boost work (no speed/style); pacing comes from punctuation
            vs = cfg.get('voice_settings')
            if vs:
                body['voice_settings'] = vs
            # request stitching: same speaker's neighbouring lines, so the read flows as one performance
            prev = [l for l in lines[:k] if l.get('speaker') == ln.get('speaker')]
            nxt = [l for l in lines[k + 1:] if l.get('speaker') == ln.get('speaker')]
            if prev:
                body['previous_text'] = prev[-1]['text']
            if nxt:
                body['next_text'] = nxt[0]['text']
            audio = call('POST', f"/v1/text-to-speech/{voice_for(ln)}?output_format=mp3_44100_128", body, raw=True)
            open(out, 'wb').write(audio)
            d = dur(out)
            flag = 'OK' if d <= ln['slot'] else f'TOO LONG by {d - ln["slot"]:.2f} s'
            print(f"{ln['id']:10} {d:5.2f} s  (slot {ln['slot']:.2f} s)  {flag}")
    elif cmd == 'mix':
        src, dst = sys.argv[2], sys.argv[3]
        ins, flt = ['-i', src], []
        for i, ln in enumerate(cfg['lines'], 1):
            p = os.path.join(HERE, 'lines', ln['id'] + '.mp3')
            ins += ['-i', p]
            d = dur(p)
            speed = max(cfg.get('tempo', 1.0), d / ln['slot'])   # base tempo, a touch more if the line is long
            speed = min(speed, 1.18)
            f = f"[{i}:a]" + (f"atempo={speed:.3f}," if speed > 1.0 else '') + f"adelay={int(ln['at'] * 1000)}:all=1[a{i}]"
            flt.append(f)
        n = len(cfg['lines'])
        flt.append(''.join(f'[a{i}]' for i in range(1, n + 1)) + f'amix=inputs={n}:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=7,apad[vo]')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', *ins, '-filter_complex', ';'.join(flt), '-map', '0:v', '-map', '[vo]',
                        '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', dst], check=True)
        print('saved', dst)
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    import urllib.parse
    main()
