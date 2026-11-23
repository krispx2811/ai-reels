"""verify.py: hear what the voice actually said. Transcribes every line with Whisper (local) and compares it
word by word with the script (diacritics, tatweel, punctuation and [audio tags] removed, alef/yaa/taa forms unified).
usage: python verify.py [model]   (default model: large-v3-turbo; first run downloads it)"""
import difflib, json, os, re, subprocess, sys
import numpy as np
from faster_whisper import WhisperModel


def load16k(path):
    """Decode with ffmpeg to 16 kHz mono float32 (avoids PyAV version issues)."""
    raw = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', path, '-f', 's16le', '-ac', '1', '-ar', '16000', '-'])
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768.0

HERE = os.path.dirname(os.path.abspath(__file__))
cfg = json.load(open(os.path.join(HERE, 'vo.json'), encoding='utf-8'))
model = WhisperModel(sys.argv[1] if len(sys.argv) > 1 else 'large-v3-turbo', device='cpu', compute_type='int8')

DIAC = re.compile('[ؐ-ًؚ-ٰٟۖ-ۭـ]')


def norm(s):
    s = re.sub(r'\[[^\]]*\]', ' ', s)                    # audio tags
    s = DIAC.sub('', s)
    s = re.sub('[إأآا]', 'ا', s).replace('ى', 'ي').replace('ة', 'ه').replace('ؤ', 'و').replace('ئ', 'ي')
    s = re.sub(r'[^\w\s]', ' ', s)
    return s.split()


bad = 0
for ln in cfg['lines']:
    p = os.path.join(HERE, 'lines', ln['id'] + '.mp3')
    segs, _ = model.transcribe(load16k(p), language='ar', beam_size=5, vad_filter=False,
                               initial_prompt='لهجة خليجية')
    heard = ' '.join(s.text for s in segs).strip()
    a, b = norm(ln['text']), norm(heard)
    ratio = difflib.SequenceMatcher(None, a, b).ratio()
    diff = [f'{" ".join(a[i1:i2]) or "∅"} → {" ".join(b[j1:j2]) or "∅"}'
            for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b).get_opcodes() if op != 'equal']
    flag = 'OK ' if ratio >= 0.8 else 'CHECK'
    bad += flag != 'OK '
    print(f'{flag} {ln["id"]:10} {ratio:.2f} | heard: {heard}')
    for d in diff:
        print(f'          diff: {d}')
print('lines to check:', bad)
