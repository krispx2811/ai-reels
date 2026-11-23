"""Print when each voice line starts and ends after the tempo change (what the subtitles must follow)."""
import json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
c = json.load(open(os.path.join(HERE, 'vo.json'), encoding='utf-8'))
rows = []
for l in c['lines']:
    d = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0',
                                       os.path.join(HERE, 'lines', l['id'] + '.mp3')]))
    sp = min(max(c.get('tempo', 1.0), d / l['slot']), 1.18)
    e = d / sp
    rows.append((l['id'], l['at'], l['at'] + e, sp))
    print(f"{l['id']:12} start {l['at']:5.2f}  end {l['at'] + e:5.2f}  x{sp:.2f}")
for a, b in zip(rows, rows[1:]):
    if a[2] > b[1] - 0.03:
        print(f'OVERLAP {a[0]} ends {a[2]:.2f} after {b[0]} starts {b[1]:.2f}')
