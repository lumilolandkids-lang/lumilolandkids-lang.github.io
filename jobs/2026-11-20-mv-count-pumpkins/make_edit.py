#!/usr/bin/env python3
"""Builds edit.json for the 2026-11-20 Count to 5 pumpkins music video (16:9). Cuts given as OUTPUT seconds;
source dur = out * speed. Timeline from Lyria's sections + Gemini transcript (song.txt / check1.json).
Shot notes: s2 not used (C1 refused/failed all redos); s3 has stray pumpkins at the sides -> zoom 1.8 centred;
s4 grew 2 extra pumpkins on the left -> only crops anchored right; s8 lost pumpkins -> only its close-up 4.4-7.2;
s9 changed place -> only its close-up 3.4-7.2; s10 morphs after 4.6 s -> 0-4.4 only; s12 more pumpkins fall in after ~2.4 s."""
import json, sys

W = "runs/2026-11-20-mv-count-pumpkins"

def c(shot, start, out, speed=1.0, **kw):
    d = {"shot": shot, "start": start, "dur": round(out * speed, 3)}
    if speed != 1.0:
        d["speed"] = speed
    d.update(kw)
    d["_out"] = out
    return d

S3 = dict(zoom=1.8, x=0.5, y=0.3)
COUNT = lambda s: [c(s, 0.0, 2.4, 0.9, push=[1.0, 1.08]), c(s, 2.2, 2.6, 1.15, push=[1.1, 1.2]), c(s, 4.6, 2.4, 1.1, push=[1.0, 1.12]),
                   c(s, 0.5, 2.6, 1.3, push=[1.05, 1.2]), c(s, 3.5, 2.0, 1.4, push=[1.12, 1.25])]
sections = [
    ("hook 0-6", [c(1, 0.25, 1.1, 0.9, push=[1.0, 1.1]), c(1, 1.4, 2.4, zoom=1.1), c(1, 3.8, 2.5, push=[1.0, 1.1])]),
    ("chorus1 6-22", [c(3, 0.5, 2.9, **S3), c(11, 4.7, 2.5), c(1, 4.0, 2.8, 1.1, push=[1.1, 1.2]), c(9, 3.6, 2.6, zoom=1.3),
                      c(3, 3.6, 2.6, **S3), c(11, 5.0, 2.6, 0.85, zoom=1.05)]),
    ("one 22-34", [c(1, 0.25, 0.95, push=[1.0, 1.1]), c(1, 1.45, 1.05, 1.1, push=[1.12, 1.25]), c(4, 0.8, 2.4, zoom=1.6, x=1.0), c(4, 4.0, 1.6, zoom=1.35, x=1.0),
                   c(1, 3.6, 3.0, 1.2, push=[1.1, 1.2]), c(1, 1.5, 3.0, 1.2, push=[1.0, 1.15])]),
    ("two 34-46", COUNT(5)),
    ("chorus2 46-62", [c(3, 0.0, 2.8, 1.1, **S3), c(9, 3.4, 2.8, zoom=1.3), c(1, 3.0, 2.6, 1.1, zoom=1.2), c(11, 4.7, 2.5),
                       c(3, 4.2, 2.8, **S3), c(9, 5.0, 2.5, 0.85, zoom=1.3)]),
    ("three 62-74", COUNT(6)),
    ("four 74-86", COUNT(7)),
    ("five 86-98", [c(11, 0.0, 3.0, 1.1), c(10, 2.2, 2.2, zoom=1.05), c(9, 3.8, 2.6, zoom=1.3), c(10, 0.0, 2.6, 1.1, push=[1.0, 1.12]),
                    c(11, 4.6, 1.6, zoom=1.05)]),
    ("clap 98-108", [c(9, 3.4, 3.0, zoom=1.3), c(11, 4.6, 2.2, 1.2), c(3, 2.5, 2.6, 1.2, **S3), c(9, 5.0, 2.2, zoom=1.3)]),
    ("review 108-117", [c(10, 0.0, 2.2, 1.2, push=[1.0, 1.1]), c(11, 0.2, 2.0, 1.2), c(10, 0.5, 2.6, push=[1.0, 1.12]),
                        c(10, 1.5, 2.2, 1.1, push=[1.1, 1.25])]),
    ("answer 117-126", [c(11, 0.2, 3.65, zoom=1.12, x=0.6), c(9, 4.4, 2.6, zoom=1.3), c(11, 4.5, 2.75)]),
    ("final chorus 126-142", [c(11, 0.0, 3.0, 1.1), c(3, 1.5, 2.8, **S3), c(9, 4.0, 2.6, zoom=1.3), c(11, 4.2, 2.6, zoom=1.05),
                              c(1, 3.6, 2.4, 1.2, zoom=1.15), c(3, 4.6, 2.6, **S3)]),
    ("outro 142-149.4", [c(11, 4.8, 2.2, zoom=1.05), c(12, 0.0, 2.6, push=[1.0, 1.06]), c(12, 2.6, 2.6, zoom=1.06)]),
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

def fx(f, sec, vol, mx):
    i = cut_at(sec)
    return {"file": f, "cut": i, "offset": round(sec - starts[i], 3), "vol": vol, "max": mx}

edit = {
    "workdir": W, "out": sys.argv[1] if len(sys.argv) > 1 else "final.mp4", "song": "song.mp3", "song_start": 0.0,
    "size": [1920, 1080], "cuts": cuts,
    "sfx": [
        fx("sfx/sparkle_chime.mp3", 0.25, 0.5, 1.0),
        fx("sfx/pop.mp3", 34.5, 0.5, 0.6), fx("sfx/pop.mp3", 62.0, 0.5, 0.6), fx("sfx/pop.mp3", 74.0, 0.5, 0.6),
        fx("sfx/question_boing.mp3", 114.0, 0.6, 0.62),
        fx("sfx/toddlers_cheer_clap.mp3", 117.1, 0.55, 2.1),
    ],
    "bounce": {"amp": 0.03, "ranges": [[6, 22], [46, 62], [98, 108], [126, 142]]},
    "vfx": [
        {"type": "sparkle", "t": 0.25, "x": 0.78, "y": 0.42, "size": 0.6, "arc": [-60, 60], "flash": False},
        {"type": "sparkle", "t": 22.1, "x": 0.78, "y": 0.45, "size": 0.7, "arc": [-60, 60]},
        {"type": "sparkle", "t": 34.6, "x": 0.2, "y": 0.45, "size": 0.7, "arc": [120, 240]},
        {"type": "sparkle", "t": 62.1, "x": 0.88, "y": 0.58, "size": 0.7, "arc": [-60, 60]},
        {"type": "sparkle", "t": 74.1, "x": 0.87, "y": 0.6, "size": 0.7, "arc": [-60, 60]},
        {"type": "sparkle", "t": 86.6, "x": 0.9, "y": 0.58, "size": 0.7, "arc": [-60, 60]},
        {"type": "confetti", "t": 98.4, "dur": 2.4, "keep_out": [0.5, 0.5, 0.4, 0.55]},
        {"type": "confetti", "t": 117.2, "dur": 2.6, "keep_out": [0.22, 0.35, 0.15, 0.3]},
        {"type": "hearts", "t": 142.4, "x": 0.15, "y": 0.9},
        {"type": "hearts", "t": 142.6, "x": 0.85, "y": 0.9},
    ],
}
print(json.dumps(edit)[:0])
json.dump(edit, open(f"{W}/edit.json" if len(sys.argv) < 3 else sys.argv[2], "w"), indent=1)
