# Crayon Babies — one autopilot run

Everything is in English (titles, descriptions, tags, prompts). No Arabic anywhere.

1. **Credits.** Call ViewMax `get_credits`. One video = 3 shots × 16 = 48 credits.
   If remaining < 48: send a push notification "ViewMax credits low: N left, video skipped", append a
   `skipped: low credits` line to `log/videos.jsonl`, and stop.
2. **Idea.** Read `log/videos.jsonl` and pick a fresh idea not used before (simple toddler story with
   Jimmy and Ava: daily routines, colors, animals, sharing, bedtime, playground, weather, etc.).
3. **Shots.** Write 3 cinematic shot prompts (~8s each) that form one mini story: beginning, middle, payoff.
   Each prompt: soft 3D Pixar-like animation, warm lighting, camera move, action, setting, mood,
   "no text, no subtitles, no speech, gentle ambient sounds only". Always describe the characters:
   - **Jimmy**: chubby 1-year-old baby boy, fluffy curly ginger hair, big blue eyes, light freckles, rosy cheeks, barefoot, light blue SHORT-SLEEVE onesie with a small yellow star.
   - **Ava**: chubby 1-year-old baby girl, short fluffy curly brown hair, small curly ponytail on top with a sparkly pink star clip, big brown eyes, rosy cheeks, soft yellow dress with ruffle sleeves and a small pink flower, pink baby shoes with bows.
4. **Video.** For each shot: ViewMax `generate_video` with model `viewmax-c1`, mode `reference-to-video`,
   `image_urls` = the two character reference URLs below, resolution `768P`, duration `8s`, aspect_ratio `9:16`,
   and an `idempotency_key` like `cb-<date>-<slug>-shotN`. Then `wait_for_task` and collect the mp4 URLs.
   If a shot fails, retry it once with the same key + `-r1`. Do NOT use Veo models: they reject any shot with babies.
   Shot 1 is always a HOOK: something magical bursts out of the paper in the first second, big reaction, short exciting line.
5. **Job file.** Write `jobs/<date>-<slug>.json` with idea, title (pattern `Baby Jimmy's Magic Crayon! 🖍️ <HOOK> <emoji> #shorts`),
   description (2–3 friendly sentences + "Made with AI animation."), ~11 tags starting with `crayon babies`, playlist "Magic Crayon Stories", shot_prompts, clips,
   viewmax_credits_before, viewmax_credits_used.
6. **Pipeline.** Run `python3 pipeline.py jobs/<file>.json`. It extracts frames, writes a music prompt,
   generates music with Lyria (Gemini API), edits with ffmpeg, uploads as public, madeForKids, synthetic
   media, and logs to `log/videos.jsonl`.
   - Exit 3 = Gemini 402/429: send a push notification "Top up $5 for Gemini API on project Video Autopilot".
   - Any other non-zero exit: send a push notification with the error line.
7. Commit and push `log/` and `jobs/`, then reply with the YouTube link.

Character reference images:
- Ava: https://lumilolandkids-lang.github.io/characters/eva.png
- Jimmy: https://lumilolandkids-lang.github.io/characters/jimmy.png
