#!/usr/bin/env python3
"""Kid-friendly visual effects pass for Crayon Babies edits (her request, 6 Nov 2026: "add moves/effects that attract children").

Used by montage.py build when edit.json has "bounce" and/or "vfx". No text ever (no on-screen words rule).
  "bounce": {"amp": 0.03, "ranges": [[6, 22], [52, 68]]}   picture pops a little on every beat of the song
                                                            (beats found with librosa; ranges in output seconds)
  "vfx": [ {"type": "sparkle",  "cut": 3, "offset": 0.2, "x": 0.62, "y": 0.45, "size": 1.0},
           {"type": "confetti", "t": 125.0, "dur": 2.4},
           {"type": "hearts",   "cut": 40, "offset": 0.0, "x": 0.5, "y": 0.7} ]
   sparkle  = golden/pink star burst + soft flash, 0.9 s, at x/y (fractions of the frame) – item appears, bubble pops;
              "arc": [a0, a1] limits the star directions in degrees (0 = right, 90 = down, 270 = up) so they fly AWAY
              from the face; "size" scales it (1.0 = burst ~1/3 of the frame height)
   confetti = colorful confetti falls over the frame, ~2.4 s – answers, "Yay!", final chorus; "keep_out": [x, y, rx, ry]
              (fractions) = the face zone where no confetti is drawn (default [0.5, 0.36, 0.15, 0.28] = a centred face)
   hearts   = small pink/red hearts float up from x/y, 1.6 s – kindness, love, thank you
Keep sparkles BESIDE faces (on the item), never on the eyes; about 6–12 effects in a 2:30 video.
"""
import math, random, subprocess
from PIL import Image, ImageDraw, ImageFilter

PALETTE = [(255, 210, 31), (255, 120, 170), (120, 200, 255), (130, 230, 170), (255, 150, 110), (190, 140, 255)]


def beats_for(song, ss, total):
    import librosa
    y, sr = librosa.load(str(song), sr=22050, offset=ss, duration=total + 0.5)
    _, b = librosa.beat.beat_track(y=y, sr=sr, units="time")
    return [float(x) for x in b]


def star(draw, cx, cy, r, color, alpha):
    pts = []
    for k in range(8):
        a = math.pi / 4 * k - math.pi / 2
        rr = r if k % 2 == 0 else r * 0.28
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    draw.polygon(pts, fill=color + (int(255 * alpha),))


def heart(draw, cx, cy, s, color, alpha):
    c = color + (int(255 * alpha),)
    draw.ellipse([cx - s, cy - s * 0.8, cx, cy + s * 0.2], fill=c)
    draw.ellipse([cx, cy - s * 0.8, cx + s, cy + s * 0.2], fill=c)
    draw.polygon([(cx - s * 0.97, cy - s * 0.15), (cx + s * 0.97, cy - s * 0.15), (cx, cy + s * 1.05)], fill=c)


class Effect:
    def __init__(self, e, t0, W, H, seed):
        self.e, self.t0, self.W, self.H = e, t0, W, H
        self.kind = e["type"]
        self.dur = float(e.get("dur", {"sparkle": 0.9, "confetti": 2.4, "hearts": 1.6}[self.kind]))
        rnd = random.Random(seed)
        sz = float(e.get("size", 1.0)) * H
        self.cx, self.cy = float(e.get("x", 0.5)) * W, float(e.get("y", 0.5)) * H
        if self.kind == "sparkle":
            a0, a1 = (math.radians(v) for v in e.get("arc", [0, 360]))  # directions: 0 = right, 90 = down, 270 = up
            self.p = [(rnd.uniform(a0, a1), rnd.uniform(0.22, 0.42) * sz, rnd.uniform(0.05, 0.085) * sz,
                       rnd.choice(PALETTE[:2] + [(255, 255, 255), (255, 235, 120)])) for _ in range(16)]
            self.flash = bool(e.get("flash", True))  # false when x/y is on a face
            self.size = sz
        elif self.kind == "confetti":
            self.p = [(rnd.uniform(0, W), rnd.uniform(-0.5 * H, -0.02 * H), rnd.uniform(0.55, 0.9) * H, rnd.uniform(34, 58) * H / 1080,
                       rnd.uniform(0, 360), rnd.uniform(-400, 400), rnd.choice(PALETTE), rnd.random() < 0.35,
                       rnd.uniform(0, 6.28)) for _ in range(int(e.get("count", 140)))]
        else:  # hearts
            self.p = [(rnd.uniform(-0.1, 0.1) * W, rnd.uniform(0.0, 0.5), rnd.uniform(34, 58) * H / 1080,
                       rnd.choice([(255, 90, 130), (255, 140, 180), (240, 60, 90)]), rnd.uniform(0, 6.28)) for _ in range(12)]

    def active(self, t):
        return self.t0 <= t <= self.t0 + self.dur

    def draw(self, layer, t):
        d = ImageDraw.Draw(layer)
        u = (t - self.t0) / self.dur
        if self.kind == "sparkle":
            ease = 1 - (1 - u) ** 3
            fade = 1.0 if u < 0.55 else max(0.0, 1 - (u - 0.55) / 0.45)
            if self.flash and u < 0.35:  # soft flash
                g = self.size * (0.08 + 0.18 * u / 0.35)
                d.ellipse([self.cx - g, self.cy - g, self.cx + g, self.cy + g], fill=(255, 250, 220, int(150 * (1 - u / 0.35))))
            for a, dist, r, col in self.p:
                x = self.cx + math.cos(a) * dist * ease
                y = self.cy + math.sin(a) * dist * ease
                star(d, x, y, r * (0.6 + 0.6 * math.sin(math.pi * min(u * 1.4, 1))), col, fade)
        elif self.kind == "confetti":
            tt = t - self.t0
            kx, ky, krx, kry = self.e.get("keep_out", [0.5, 0.36, 0.15, 0.28])  # face zone (fractions): no confetti there
            kx, ky, krx, kry = kx * self.W, ky * self.H, krx * self.W, kry * self.H
            fade = 1.0 if u < 0.8 else max(0.0, 1 - (u - 0.8) / 0.2)
            for x0, y0, v, s, rot0, vr, col, circ, ph in self.p:
                y = y0 + v * tt
                x = x0 + 40 * math.sin(ph + tt * 3)
                if ((x - kx) / krx) ** 2 + ((y - ky) / kry) ** 2 < 1.0:
                    continue
                if circ:
                    d.ellipse([x - s * 0.45, y - s * 0.45, x + s * 0.45, y + s * 0.45], fill=col + (int(235 * fade),))
                else:
                    a = math.radians(rot0 + vr * tt)
                    w, h = s * 0.5, s * 0.25 * (0.3 + abs(math.cos(a * 1.7)))
                    pts = [(x + px * math.cos(a) - py * math.sin(a), y + px * math.sin(a) + py * math.cos(a))
                           for px, py in ((-w, -h), (w, -h), (w, h), (-w, h))]
                    d.polygon(pts, fill=col + (int(235 * fade),))
        else:
            for dx, delay, s, col, ph in self.p:
                k = max(0.0, (u - delay * 0.5) / (1 - delay * 0.5))
                if k <= 0:
                    continue
                x = self.cx + dx + 25 * math.sin(ph + k * 6)
                y = self.cy - k * 0.45 * self.H
                fade = 1.0 if k < 0.6 else max(0.0, 1 - (k - 0.6) / 0.4)
                heart(d, x, y, s * (0.6 + 0.6 * min(k * 3, 1)), col, fade)


def apply(video_in, video_out, edit, starts, song, ss, total, fps=24):
    W, H = edit.get("size", [1080, 1920])
    bounce = edit.get("bounce")
    beats = beats_for(song, ss, total) if (bounce and song) else []
    amp = float((bounce or {}).get("amp", 0.03))
    ranges = (bounce or {}).get("ranges") or [[0, total]]
    effects = []
    for k, e in enumerate(edit.get("vfx", [])):
        t0 = float(e["t"]) if "t" in e else starts[int(e["cut"])] + float(e.get("offset", 0))
        effects.append(Effect(e, t0, W, H, 1000 + k))
    dec = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(video_in), "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                           stdout=subprocess.PIPE)
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                            "-r", str(fps), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "17",
                            "-pix_fmt", "yuv420p", str(video_out)], stdin=subprocess.PIPE)
    n, fb = 0, W * H * 3
    bi = 0
    while True:
        buf = dec.stdout.read(fb)
        if len(buf) < fb:
            break
        t = n / fps
        im = Image.frombuffer("RGB", (W, H), buf)
        z = 1.0
        if beats and any(a <= t <= b for a, b in ranges):
            while bi + 1 < len(beats) and beats[bi + 1] <= t:
                bi += 1
            if beats[bi] <= t:
                z = 1 + amp * math.exp(-(t - beats[bi]) / 0.13)
        if z > 1.0005:
            cw, ch = W / z, H / z
            x0, y0 = (W - cw) / 2, (H - ch) / 2 * 0.85
            im = im.resize((W, H), Image.BICUBIC, box=(x0, y0, x0 + cw, y0 + ch))
        act = [e for e in effects if e.active(t)]
        if act:
            layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            for e in act:
                e.draw(layer, t)
            glow = layer.filter(ImageFilter.GaussianBlur(6))
            im = Image.alpha_composite(Image.alpha_composite(im.convert("RGBA"), glow), layer).convert("RGB")
        enc.stdin.write(im.tobytes())
        n += 1
    enc.stdin.close()
    enc.wait()
    dec.wait()
    print(f"[vfx] {n} frames, {len(beats)} beats, {len(effects)} effects")
