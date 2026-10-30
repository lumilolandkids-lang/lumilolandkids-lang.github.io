# Crayon Babies — YouTube thumbnail with Gemini (Nano Banana 2)

Her choice (29 Oct 2026): thumbnails are DESIGNED with Google's Gemini image model (Nano Banana 2 in ViewMax,
0 credits inside the daily pool), not cut from a video frame. Used for the long videos (Friday music video,
Sunday compilation). Channel bible section 10: big close-up faces with strong emotion, the problem/song object,
2–4 words of huge rounded text that match the hook, bright simple background, the exact outfits used.

## 1. Generate (one call, retry at most twice)
`generate_image` model `nano-banana-2`, aspect_ratio `16:9`, quality `2K`, idempotency_key `cb-<date>-<slug>-thumb`
(`-r1`, `-r2` for retries). image_urls (max ~6): 1–2 of the video's best approved start frames (the strongest
emotion/moment) + the reference sheet of every character shown (section 5 links).

Prompt template (fill the brackets, copy identity keys in CAPS from section 13):
```
Create an eye-catching YouTube thumbnail, wide 16:9, in the exact same 3D Pixar style and with the exact same
characters as the uploaded images (images 1-2 = scenes from the video, the others = character reference sheets).
[MAIN ACTION, e.g. "In the center, a big close-up of SUNNY THE LION CUB roaring proudly with his mouth wide open –
cute, friendly and never scary."] On the left BABY JIMMY ([identity keys + outfit]) and on the right BABY AVA
([identity keys + outfit]), both with huge [excited/surprised] happy faces, eyes wide open. All faces large, sharp
and facing the camera. Background: [the place from the video] softly blurred. At the top, huge bold rounded playful
text exactly "[2-4 WORDS IN CAPS]" in bright yellow with a thick purple outline, perfectly spelled, easy to read on
a small phone screen. Vibrant colors, high contrast, clean simple composition, no other text, no logos, no watermark.
```

## 2. Check (mandatory)
Download (`curl -sSL -o`) and LOOK at it at full size and with face crops:
- every identity key right (Jimmy GINGER hair + BLUE eyes + FRECKLES; Ava BROWN hair + pink STAR clip + BROWN eyes …),
- the words spelled exactly, nothing else written, no extra fingers/limbs, nothing scary.
Any miss → regenerate (max 2 retries), then keep the best one.

## 3. Fit for YouTube
`python3 compile.py fit IN.png OUT.jpg` → 1280×720 JPG under 2 MB. Put OUT.jpg in the job's `thumbnail`.
Fallback only if Nano Banana fails 3 times: `python3 compile.py thumb <final.mp4> <sec> "<WORDS>" OUT.jpg`.
