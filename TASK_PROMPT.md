# Crayon Babies — one autopilot run

Everything is in English (titles, descriptions, tags, prompts). No Arabic anywhere.

1. **Credits.** Call ViewMax `get_credits`. One video = 3 shots × 40 = 120 credits.
   If remaining < 120: send a push notification "ViewMax credits low: N left, video skipped", append a
   `skipped: low credits` line to `log/videos.jsonl`, and stop.
2. **Idea.** Read `log/videos.jsonl` and pick a fresh idea not used before (simple toddler story with
   Jimmy and Eva: daily routines, colors, animals, sharing, bedtime, playground, weather, etc.).
3. **Shots.** Write 3 cinematic shot prompts (~8s each) that form one mini story: beginning, middle, payoff.
   Each prompt: soft 3D Pixar-like animation, warm lighting, camera move, action, setting, mood,
   "no text, no subtitles, no speech, gentle ambient sounds only". Always describe the characters:
   - **Jimmy**: baby boy, bright orange curly hair, big blue eyes, freckles, blue short-sleeve bodysuit with a yellow star, barefoot.
   - **Eva**: toddler girl, auburn curly hair in a small top bun with a pink star clip, big brown eyes, yellow flutter-sleeve dress with a pink flower, pink shoes with bows.
4. **Video.** For each shot: ViewMax `generate_video` with model `veo-3-1-fast`, mode `reference-to-video`,
   `image_urls` = the two character reference URLs below, resolution `1080p`, aspect_ratio `9:16`,
   and an `idempotency_key` like `cb-<date>-<slug>-shotN`. Then `wait_for_task` and collect the mp4 URLs.
   If a shot fails, retry it once with the same key + `-r1`.
5. **Job file.** Write `jobs/<date>-<slug>.json` with idea, title (≤70 chars, catchy, include #shorts),
   description (2–3 friendly sentences + "Made with AI animation."), 8–12 tags, shot_prompts, clips,
   viewmax_credits_before, viewmax_credits_used.
6. **Pipeline.** Run `python3 pipeline.py jobs/<file>.json`. It extracts frames, writes a music prompt,
   generates music with Lyria (Gemini API), edits with ffmpeg, uploads as public, madeForKids, synthetic
   media, and logs to `log/videos.jsonl`.
   - Exit 3 = Gemini 402/429: send a push notification "Top up $5 for Gemini API on project Video Autopilot".
   - Any other non-zero exit: send a push notification with the error line.
7. Commit and push `log/` and `jobs/`, then reply with the YouTube link.

Character reference images:
- Eva: https://lumilolandkids-lang.github.io/characters/eva.png
- Jimmy: https://lumilolandkids-lang.github.io/characters/jimmy.png
