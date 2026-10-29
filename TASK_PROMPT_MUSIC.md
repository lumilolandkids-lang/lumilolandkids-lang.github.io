# Crayon Babies — one automated MUSIC-CLIP Short (approved format, Oct 2026)

The scheduled prompt says **MODE: TEST** or **MODE: LIVE** (and, for LIVE, the publish time).
- TEST = do everything except the YouTube upload; deliver the video in the repo.
- LIVE = upload with `upload_ready.py`, scheduled with `publish_at`.

**Quality rule:** this run uses the newest Claude model. Work at extra-high effort on every prompt, lyric, title
and description: plan, draft, check it line by line against the channel bible, improve, then use it.
Nobody is watching: never ask questions — decide and continue. Everything you write is in English.

**Channel bible:** load the skill `crayon-babies-channel` with the Skill tool. If it isn't installed, read
`skills/crayon-babies-channel/SKILL.md` in this repo. Follow section 1 (rules), 2–5 (characters, places, reference
links — copy descriptions word for word), 8 (songs), 10 (titles), 13 (identity lock + montage).

Work folder `W = runs/<date>-<slug>` (git-ignored). Date = today in UTC, `YYYY-MM-DD`.

## 1. Credits
ViewMax `get_credits`. Needed ≥ 130 (5 shots × 14 + up to 3 new sound effects × 5 + margin). If less: push
notification "ViewMax credits low: N left – video skipped", append `{"time":..,"status":"skipped: low credits"}` to
`log/videos.jsonl`, commit, push, stop.

## 2. Idea and plan (extra-high effort)
- ONE new idea from the idea bank (section 6) or a fresh one in the same spirit. It must not repeat any idea in
  `log/videos.jsonl` or the "Done" lists. Seasonal ideas win when the date fits.
- Jimmy and Ava are the stars; at most ONE more character (a pet, Leo/Mia, Mommy Lily or Daddy Tom).
  ONE place that has an online reference image (section 5). Pick outfits from the lists.
- 5 shots × 10 s: 1 **HOOK** (problem or surprise in the first second, close-up, big reaction) · 2 the problem /
  first try · 3 help or idea · 4 the big happy solution moment · 5 **LOOP ENDING** (mirror of shot 1, problem solved,
  "Bye bye!"). One simple lesson.
- Write `W/plan.json`: idea, lesson, place, characters + outfits, shots[{role, frame_prompt, motion_prompt}],
  song (style + timestamped lyrics), sound effects wanted, title, description, tags, playlist.

## 3. Start frames — Nano Banana 2 (section 13, Step 1)
`generate_image` model `nano-banana-2`, aspect_ratio `9:16`, quality `2K`, image_urls = the character sheets in the
shot + the place image (links in section 5), and for shots 2–4 ALSO the approved hook frame as identity anchor.
idempotency_key `cb-<date>-<slug>-f<N>` (retries `-r1`, `-r2`). `wait_for_task` for the URL.
- Every frame prompt: "3D Pixar style", the character descriptions + outfits word for word, the identity keys in
  CAPS (section 13), the place block word for word, medium close-up, faces large (≥ 1/5 of the frame height),
  eyes open, faces separate (no hugs, no cheeks pressed together), exactly two hands each, no text.
- Shot 5 = EDIT of the hook frame: image_urls = [hook frame, + the same sheets], prompt "Keep EVERYTHING in image 1
  exactly the same … ONLY CHANGE: …".

## 4. FACE CHECK — mandatory before animating (Step 2)
Download each frame (`curl -sSL -o`), crop every face at full resolution (ffmpeg crop or PIL) and LOOK at the crops
with the Read tool. Tick every identity key (hair color/shape, EYE COLOR, freckles, star clip, outfit details, place
details). Any miss → regenerate that frame (free; at most 3 tries per frame, then keep the best one).

## 5. Animate — Seedance 1.0 Pro (Step 3)
`generate_video` model `seedence-1-0-pro`, mode `image-to-video`, image_urls = [frame URL], resolution `1080p`,
duration `10s`, idempotency_key `cb-<date>-<slug>-s<N>`. Motion prompt: identity keys in CAPS, small gentle movements,
still camera, NO hugging, turning around, covering faces, long closed-eye laughing or anything passing in front of
a face. Silent. `wait_for_task`, then `curl -sSL -o W/shotN.mp4 <url>`.

## 6. Clip check (Step 4)
`python3 montage.py faces W N 3 6 9.5` for every shot → look at the frames vs the start frame. If a shot drifted,
redo only that shot once (`-r1`, 14 credits). Never more than one redo in the whole run.

## 7. Song — Lyria clip, 30 s (section 8 style)
Write `W/song_prompt.txt`: the section 8 style (a cappella children's voices, humming and "la la", ONLY daf and hand
claps, ~110 BPM, major key, a sweet little boy and girl singing slowly and clearly in simple English).
  **NO musical instruments at all** (her firm rule, for religious reasons): only children's voices singing, humming and "la la", mouth sounds (soft beatbox, "boom-chk", tongue clicks), hand claps, finger snaps and a daf/frame drum. Write in the prompt: "NO instruments: no piano, no guitar, no ukulele, no bells, no xylophone, no synth, no strings, no flute, no electronic beats".
   + the lyrics
with timestamps so each line lands on its beat, e.g.
`[0:00 - 0:03] Hook: "Oh no! ..."` … `[0:26 - 0:30] Outro: "Bye bye, friends!"`.
Short lines, repetition, the lesson as the chorus. Then:
`python3 song.py W/song_prompt.txt W/song.mp3` (model `lyria-3-clip-preview`, exactly 30 s, about 8 US cents).
- Exit 3 = Gemini prepaid credits empty/quota → continue with NO song (`"song": null`) and say so in the notification.
- Other error: read it; if the Interactions API response shape changed, fix `song.py`, commit the fix, retry once.
- You cannot hear audio: never claim it sounds good. Check the duration and that mean_volume is not silent.
- Find where the singing starts: `ffmpeg -i W/song.mp3 -af silencedetect=n=-35dB:d=0.3 -f null -` → `song_start`.

## 8. Sound effects
Reuse `sfx/*.mp3` (see `sfx/README.md`). Generate at most 3 new ones for this story's special moments with
`generate_sound_effect` (5 credits each, idempotency keys `cb-<date>-<slug>-fx<N>`); download them into W.
Save reusable ones into `sfx/` with a row in `sfx/README.md`.

## 9. Edit plan — the approved montage (Step 5)
`python3 montage.py sheets W` → LOOK at every sheet. Then write `W/edit.json` (format in `montage.py` docstring):
- 10–14 cuts of 1.2–3.5 s, total ≈ 30 s (the song length). Hook = the strongest 1–1.5 s at `speed` 0.6–0.75.
  A second cut from the same shot gets `zoom` 1.10–1.12. Skip blinks, look-downs, blur, drift, extra hands.
  End on shot 5 (the loop shot).
- **NO on-screen words** (her rule, 29 Oct 2026: text like "ROAR?" / "Meow?!" looked out of place). Never set
  `show_words`; the picture, the song and the sound effects tell the story.
- Effects on the exact visual moments (mouth opens, clap, pop…) read from the sheets; character sounds vol 0.5–1.0.
`python3 montage.py build W/edit.json` → `W/final.mp4`, `W/final_sheet.jpg`, `W/final_hook.jpg`.
LOOK at both sheets (first 2 s especially, no text on screen, no bad frames, identity OK). Fix edit.json and rebuild
if needed (free). Final file name for people: `Crayon Babies - <Title>.mp4`.

## 10. Title, description, tags (section 10)
English + emoji title with the hook first; description template with NO hashtags; 11–15 tags starting with
`crayon babies, baby jimmy, baby ava`; playlist "Crayon Babies Songs". Write `jobs/<date>-<slug>.json`:
`{"idea", "video": "ready/<date>-<slug>.mp4", "title", "description", "tags", "playlist", "publish_at", "viewmax_credits_used"}`.
Also save everything needed to REBUILD this short later (the Sunday compilation rebuilds the week's shorts; the
mp4 itself is not kept in the repo) into `jobs/<date>-<slug>/`: `plan.json`, `edit.json`, `song_prompt.txt`
(+ `song.txt`), `song.mp3`, any new effect files used by edit.json, and `shots.json` =
`{"shot1": "<seedance mp4 url>", ..., "frames": {"f1": "<frame url>", ...}}`. In this copy of edit.json set
`"workdir"` to `"runs/<date>-<slug>"` (relative) and point `song`/effect paths at files that exist in
`jobs/<date>-<slug>/` or `sfx/` (montage.py looks in the workdir first, then the repo root).

## 11. Deliver
- **TEST:** copy `W/final.mp4` to `ready/test-<date>-<slug>.mp4` and `W/final_sheet.jpg` to
  `ready/test-<date>-<slug>.jpg`. Commit (jobs/, sfx/, ready/ test files, any script fixes) and push to `autopilot`.
  Do NOT upload to YouTube. Push notification: "TEST video ready: <title>" + one line on the song (OK / no song + why).
- **LIVE:** copy to `ready/<date>-<slug>.mp4`, set `publish_at` from the scheduled prompt, run
  `python3 upload_ready.py jobs/<date>-<slug>.json`. Upload once only (retry once only if it failed before a video id
  was printed). Commit and push `log/` and `jobs/` (and sfx/ additions). Push notification: title + YouTube link +
  publish time. Then remove the mp4 from `ready/` in a follow-up commit (YouTube has it; keep the repo small).

## 12. Finish
Short summary: idea, title, ViewMax credits used / remaining, song OK?, sound effects used, any problem and what you
did about it. Never print the values of GEMINI_API_KEY, YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN.
