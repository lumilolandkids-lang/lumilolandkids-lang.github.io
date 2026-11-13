#!/usr/bin/env python3
"""Builds edit.json for the 2026-11-13 Shapes Song music video (16:9). Cuts are given as OUTPUT seconds;
source dur = out * speed. Timeline follows Lyria's section timestamps (song.txt)."""
import json, sys
from pathlib import Path

W = "runs/2026-11-13-mv-shapes-song"

def c(shot, start, out, speed=1.0, **kw):
    d = {"shot": shot, "start": start, "dur": round(out * speed, 3)}
    if speed != 1.0:
        d["speed"] = speed
    d.update(kw)
    d["_out"] = out
    return d

sections = [
    ("hook 0-6", [c(1, 0.2, 1.6, 0.9, push=[1.0, 1.12]), c(1, 1.6, 2.4, zoom=1.1), c(1, 4.0, 2.0)]),
    ("chorus1 6-22", [c(2, 0.3, 3.0), c(3, 0.5, 3.0, 1.1), c(8, 0.3, 2.6), c(2, 3.5, 3.0), c(3, 4.0, 2.6), c(8, 3.8, 1.8)]),
    ("circle 22-38", [c(4, 0.0, 3.0), c(1, 2.5, 2.5, zoom=1.15), c(4, 3.0, 3.0), c(1, 5.0, 2.0, push=[1.0, 1.15]),
                      c(4, 5.0, 2.2), c(4, 1.0, 3.3, 1.2, zoom=1.12)]),
    ("square 38-54", [c(5, 0.0, 2.0, 0.9), c(5, 1.8, 3.0), c(5, 4.8, 2.4, zoom=1.12), c(5, 0.5, 3.0, 1.2, push=[1.1, 1.25]),
                      c(5, 3.5, 3.2, 1.1, zoom=1.2, x=0.3), c(5, 2.5, 2.4, 1.3)]),
    ("chorus2 54-70", [c(3, 0.0, 2.8, 1.1), c(2, 1.0, 3.0, zoom=1.1), c(8, 1.5, 2.6), c(3, 4.3, 2.6), c(2, 4.0, 2.8), c(8, 5.0, 2.2)]),
    ("triangle 70-86", [c(6, 0.0, 2.4), c(6, 2.4, 2.6, zoom=1.1), c(6, 5.0, 2.2), c(6, 0.5, 3.0, 1.3, push=[1.0, 1.15]),
                        c(6, 3.8, 3.2, 1.05, zoom=1.15), c(6, 1.5, 2.6, 1.4)]),
    ("star 86-102", [c(7, 1.0, 2.4, zoom=1.45, x=0.42, y=0.5), c(7, 3.4, 2.6, zoom=1.55, x=0.42, y=0.5),
                     c(10, 0.2, 2.6, 1.3, zoom=1.6, x=0.5, y=0.45), c(7, 0.2, 2.6, 1.2, push=[1.3, 1.55], x=0.42, y=0.5),
                     c(7, 3.0, 2.8, 1.3, zoom=1.4, x=0.42, y=0.5), c(10, 3.5, 3.0, 1.2, push=[1.5, 1.7], x=0.5, y=0.45)]),
    ("clap 102-114", [c(8, 0.0, 2.8), c(2, 2.0, 2.4, 1.2), c(3, 2.5, 2.4, 1.2), c(8, 2.8, 2.2, 1.1, zoom=1.1), c(2, 5.0, 2.2)]),
    ("review 114-126", [c(9, 0.0, 3.0, 1.4, push=[1.0, 1.12]), c(9, 2.0, 2.8, 1.4, push=[1.1, 1.3]), c(9, 1.5, 3.2, 1.5, push=[1.1, 1.25]),
                        c(9, 0.2, 3.0, 1.6, push=[1.25, 1.45], y=0.4)]),
    ("answer 126-134", [c(10, 0.5, 2.6, 1.2, push=[1.4, 1.65], x=0.5, y=0.45), c(10, 3.6, 2.6, 1.2, zoom=1.6, x=0.5, y=0.45), c(8, 4.0, 2.8)]),
    ("final chorus 134-152", [c(11, 0.0, 3.0), c(11, 3.0, 3.0), c(3, 1.5, 2.8), c(11, 5.5, 1.7), c(2, 2.5, 2.8, zoom=1.1),
                              c(8, 0.5, 2.4, 1.2), c(11, 4.0, 2.3, zoom=1.1)]),
    ("outro 152-159.5", [c(12, 0.0, 3.6), c(12, 3.4, 3.9, 0.95, zoom=1.08)]),
]

cuts, t, starts = [], 0.0, []
for name, cs in sections:
    for x in cs:
        assert x["start"] + x["dur"] <= 7.29, (name, x)
        starts.append(round(t, 2))
        t += x.pop("_out")
        cuts.append(x)
    print(f"{name}: ends at {t:.2f}")
print("total", round(t, 2), "cuts", len(cuts))

def cut_at(sec):
    return max(i for i, s in enumerate(starts) if s <= sec + 1e-6)

edit = {
    "workdir": W, "out": sys.argv[1] if len(sys.argv) > 1 else "final.mp4", "song": "song.mp3", "song_start": 0.0,
    "size": [1920, 1080], "cuts": cuts,
    "sfx": [
        {"file": "sfx/sparkle_chime.mp3", "cut": 0, "offset": 0.25, "vol": 0.5, "max": 1.0},
        {"file": "sfx/question_boing.mp3", "cut": cut_at(124.0), "offset": 124.0 - starts[cut_at(124.0)], "vol": 0.6, "max": 0.62},
        {"file": "sfx/toddlers_cheer_clap.mp3", "cut": cut_at(126.2), "offset": 126.2 - starts[cut_at(126.2)], "vol": 0.55, "max": 2.1},
    ],
    "bounce": {"amp": 0.03, "ranges": [[6, 22], [54, 70], [102, 114], [134, 152]]},
    "vfx": [
        {"type": "sparkle", "t": 0.25, "x": 0.74, "y": 0.25, "size": 0.6, "arc": [-60, 60], "flash": False},
        {"type": "sparkle", "t": 22.1, "x": 0.66, "y": 0.45, "size": 0.7, "arc": [-60, 60]},
        {"type": "sparkle", "t": 38.1, "x": 0.73, "y": 0.35, "size": 0.7, "arc": [-60, 60]},
        {"type": "sparkle", "t": 70.1, "x": 0.76, "y": 0.5, "size": 0.7, "arc": [-60, 60]},
        {"type": "sparkle", "t": 86.1, "x": 0.72, "y": 0.4, "size": 0.7, "arc": [-60, 60]},
        {"type": "confetti", "t": 102.0, "dur": 2.4, "keep_out": [0.5, 0.36, 0.16, 0.3]},
        {"type": "confetti", "t": 126.2, "dur": 2.6, "keep_out": [0.5, 0.4, 0.18, 0.32]},
        {"type": "hearts", "t": 152.4, "x": 0.15, "y": 0.9},
        {"type": "hearts", "t": 152.6, "x": 0.85, "y": 0.9},
    ],
}
Path(W, "edit.json").write_text(json.dumps(edit, indent=1))
print("cut starts:", starts)
