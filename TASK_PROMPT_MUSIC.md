# Crayon Babies — the daily Short (her rule 10 Nov 2026, option B: 2 clips per long video + new Shorts in the empty slots)

**Her decision, 10 Nov 2026 (she felt too many Shorts came from the bubble video):** only **2 clips** per long video
(clip 1 = the opening hook + first chorus, clip 2 = the review/question + "Bye bye, friends!" ending). Every other Short
slot makes a **NEW Short from scratch** with the old recipe below (steps 1–12: credits check ≥ 130, Lyria song FIRST,
Nano Banana frames, ViewMax C1 shots, ~100 credits). Never more than one clip of the same long video per day.
Decision order for every Short run:
1. A long video (rules in A) with fewer than 2 clips, whose publish time has passed, and no clip of it published today
   → cut the next clip (sections A–D, 0 credits).
2. Otherwise → make a NEW Short with the old recipe (steps 1–12 below). Its idea, place and song must differ from every
   earlier video AND from the current long videos (no new Short about the same topic as a long video of the last 7 days).

(History: 5–9 Nov 2026 the rule was "no new Shorts, up to 4 clips per long video"; the bubble video got 4 clips. That rule is replaced.)

## A. Pick the source
- Long videos = log entries with `"kind": "long"` (or a `-mv-` job) and `"status": "uploaded"`, from the last 21 days.
  Prefer the newest long video that has fewer than 2 clips used (count log entries with its `source_long`).
- Wait until the long video's own publish time has passed (a clip never comes out before its long video).
- None available → go to the NEW Short recipe (step 1 below). Only if that is impossible (credits < 130, Gemini song
  quota) skip and log the reason.

## B. Rebuild the long video (free)
`W = runs/<date>-clip-<slug>`. Download the long video's clips from `jobs/<long>/shots.json` into
`runs/<long>/shotN.mp4` (its edit.json workdir), copy its song.mp3 + effects, `python3 montage.py build
jobs/<long>/edit.json` → the 16:9 final.mp4. Read its song timeline (`jobs/<long>/song_prompt.txt` / song.txt).

## C. Choose the segment (extra-high effort)
- 30–45 s, self-contained: it STARTS on a strong visual moment at the start of a sung line (the first clip of every
  long video = its opening hook + first chorus), teaches ONE item/step of the song + the chorus, and ENDS at the end of
  a phrase (best: on "Bye bye, friends!" or a happy cheer). Never more than 5 s overlap with an earlier clip of the same
  long video (read `segment` of earlier log entries).
- `python3 compile.py vclip <final.mp4> START DUR W/final.mp4 [ZOOM 1.35] [X 0.5]` → 1080×1920 (picture zoomed so the
  baby is big, blurred copy above/below, its own audio with fades, NO text). Make a 1 fps contact sheet and LOOK at it:
  the baby's face big and centred (adjust X 0–1 / ZOOM 1.2–1.6), first second strong, no bad frame, no text.
  `python3 montage.py motion W/final.mp4` – every second ≥ 2.0, else move the segment.

(Effects, 6 Nov 2026: the rebuilt long video already has its bounce/sparkles/confetti from its saved edit.json – keep them in the clip.)

## D. Title, description, upload
(Growth checklist, 6 Nov 2026: `playlist` = ["Crayon Babies Songs", the long video's topic playlist "Learn with Crayon Babies" or "Good Habits for Kids"]; add the "🎶 Voices only …" description line from TASK_PROMPT_MUSIC_VIDEO.md; after the upload run `python3 stats.py`.) (NO tags – her rule, 6 Nov 2026)
- Title (bible section 10): the clip's own hook + learning goal, e.g. `Wow! Number 3! 🍎 Count with Baby Jimmy |
  Learn Numbers | Crayon Babies` – different from every earlier title.
- Description: section 10 template, NO hashtags, plus the line `🎵 From our full song "<long video title>" –
  find the full song on the Crayon Babies channel (playlist Crayon Babies Songs).`
- NO tags (her rule, 6 Nov 2026). Playlist "Crayon Babies Songs". Made for kids, AI = yes.
- `jobs/<date>-<slug>.json` with `"video": "ready/<date>-<slug>.mp4"`, `"short": true`, `"viewmax_credits_used": 0`,
  `"source_long": "<long job>"`, `"segment": [START, START+DUR]`, `publish_at` from the scheduled prompt.
  Copy W/final.mp4 to ready/, `python3 upload_ready.py jobs/<date>-<slug>.json` once. Add `source_long`, `segment`,
  `star` to its log entry. Commit + push `log/` and `jobs/`, remove the mp4 from `ready/`, push notification
  (title + link + time). Summary as in step 12.

---

# NEW Short recipe (used again from 10 Nov 2026 for every Short slot without an unused long-video clip; also the reference for the long videos' shots)

## Old Short recipe (Oct 2026)

The scheduled prompt says **MODE: TEST** or **MODE: LIVE** (and, for LIVE, the publish time).
- TEST = do everything except the YouTube upload; deliver the video in the repo.
- LIVE = upload with `upload_ready.py`, scheduled with `publish_at`.

**Quality rule:** this run uses the newest Claude model at **EXTRA-HIGH effort (effort level: extra)** — her explicit
request. Every prompt, lyric, title, description and edit decision: plan, draft, check it line by line against the
channel bible, improve, then use it. Never rush a check to save time.
Nobody is watching: never ask questions — decide and continue. Everything you write is in English.

**Channel bible:** read `skills/crayon-babies-channel/SKILL.md` in THIS repo – it is the newest version and wins over
any installed copy of the skill. Also read `LEARNING.md` (the learning calendar and checks) before planning. Follow section 1 (rules), 2–5 (characters, places, reference
links — copy descriptions word for word), 8 (songs), 10 (titles), 13 (identity lock + montage).

Work folder `W = runs/<date>-<slug>` (git-ignored). Date = today in UTC, `YYYY-MM-DD`.

## 1. Credits
ViewMax `get_credits`. Needed ≥ 130 (5 shots × 14 + up to 3 new sound effects × 5 + margin). If less: push
notification "ViewMax credits low: N left – video skipped", append `{"time":..,"status":"skipped: low credits"}` to
`log/videos.jsonl`, commit, push, stop.

## 2. Idea and plan (extra-high effort)
- **Learning first (LEARNING.md):** take today's topic from the weekly calendar (New York weekday + this run's slot:
  before 07:00 NY = slot 1, otherwise slot 2), continue series in order (next number/letter from `log/videos.jsonl`),
  then build ONE fun story around that goal with 2–3 fun mechanics (interactive pause, say-it-with-me, copy-me action,
  surprise). Fill `plan.json` → `learning` (goal, target_words, shown_how, song_repeats, interactive_moment,
  fact_check, modeling, toddler_fit). Not cute-only: a child must learn, copy or answer something.
- The idea must not repeat any idea in `log/videos.jsonl` or the "Done" lists. Seasonal ideas win when the date fits.
- **ONE BABY ONLY (her rule, 2 Nov 2026 evening – bible rule 17 + section 15):** the star is Jimmy OR Ava – the other
  baby than the `star` of the last log entry that has one (none yet → Jimmy). Never a second child. By default no other
  character; only Tue/Wed/Fri slot 2 (kindness, safety, family) may add ONE grown-up (Mommy Lily / Daddy Tom) or
  Biscuit, with their sheet in image_urls. Teach the topic with 2–3 clear items/steps; letters, numbers and shapes are
  real 3D objects in the scene (never overlay text), and no other letters/numbers anywhere in the frame. ONE place that has an online reference image (section 5). Pick outfits from the lists.
- **VARIETY (her rule, 2 Nov 2026: "I always feel they are in the same place – vary the places, add the other
  characters, always vary"):** before choosing, list the place, star and outfits of the last 6 entries in
  `log/videos.jsonl`. The place must NOT be any of the last 3 videos' places (until 2 Nov: playroom, backyard and
  living room were overused). Rotate through ALL places: kitchen, bathroom, Jimmy's room, Ava's room, house outside,
  SUNNY PARK, THE SUPERMARKET, DR. HANA'S CLINIC, LITTLE STARS NURSERY (reference images), and also THE BEACH, GRANDMA'S
  FARM, THE ZOO, THE LIBRARY, THE MALL (text-only blocks from section 4 – fine for frames). (The "one extra character in every video" part was replaced the
  same evening by the ONE BABY rule above.) Outfits change with the place (park = OUTDOOR, kitchen = CHEF,
  bed = PAJAMAS, …). Write `"star"` and `"variety": {"place", "star", "last_places"}` in plan.json and the log entry.
- 5 shots × 10 s in the ORGANIZED learning order of bible section 15: 1 **HOOK** (the first item appears by surprise
  right in front of the baby, close-up, big reaction) · 2 item/step 1 · 3 item/step 2 · 4 item/step 3, or all items in a
  neat row + the question to the viewer · 5 **LOOP ENDING** (mirror of shot 1, all items in a row, "Bye bye!"). Items
  come in the same order in shots and song, each appears only from its own shot on. One clear learning goal.
- Write `W/plan.json`: idea, lesson, place, characters + outfits, shots[{role, frame_prompt, motion_prompt}],
  song (style + timestamped lyrics), sound effects wanted, title, description, tags, playlist.

## 2b. SONG FIRST — before spending any ViewMax credit
Do step 7 (the Lyria song) right now, before any frame or shot. If `song.py` exits 3 (Gemini billing/quota, e.g.
"limit: 0 requests per day on Free Tier"), STOP the whole run: no frames, no shots, no credits spent. Append
`{"time":..,"status":"skipped: gemini song quota/billing","error":"<line>"}` to `log/videos.jsonl`, commit, push, and send
the push notification "Video skipped – Gemini song not available (check AI Studio → Billing, project Video Autopilot)".
A video is never published without its song.

## 3. Start frames — Nano Banana 2 (section 13, Step 1)
`generate_image` model `nano-banana-2`, aspect_ratio `9:16`, quality `2K`, image_urls = the character sheets in the
shot + the place image (links in section 5), and for shots 2–4 ALSO the approved hook frame as identity anchor.
idempotency_key `cb-<date>-<slug>-f<N>` (retries `-r1`, `-r2`). `wait_for_task` for the URL.
- Every frame prompt: "3D Pixar style", the character descriptions + outfits word for word, the identity keys in
  CAPS (section 13), the place block word for word, medium close-up, faces large (≥ 1/5 of the frame height; one baby: ≥ 1/4, the item beside the face),
  eyes open, faces separate (no hugs, no cheeks pressed together), exactly two hands each, no text.
- Shot 5 = EDIT of the hook frame: image_urls = [hook frame, + the same sheets], prompt "Keep EVERYTHING in image 1
  exactly the same … ONLY CHANGE: …".
- **STORY ORDER (her correction, 30 Oct 2026):** anything the characters draw, make, fix or bring must NOT be visible
  in any frame or cut before that moment. Write a before/after table in plan.json (e.g. tail: shots 1–2 absent, shot 3
  being drawn, shots 4–5 present). The "doing it" frame shows the action STARTING (crayon touching the empty spot,
  nothing drawn yet); its motion prompt says the part is drawn line by line following the crayon tip. Never give that
  frame the finished result.

## 4. FACE CHECK — mandatory before animating (Step 2)
Download each frame (`curl -sSL -o`), crop every face at full resolution (ffmpeg crop or PIL) and LOOK at the crops
with the Read tool. Tick every identity key (hair color/shape, EYE COLOR, freckles, star clip, outfit details, place
details). Also check the LEARNING facts in the frame: object counts match the number in the song, colors/shapes/
letters are right. Any miss → regenerate that frame (free; at most 3 tries per frame, then keep the best one).
**SIDE-BY-SIDE WITH THE SHEET (her note, 1 Nov 2026 – "Jimmy and Ava don't look like usual"):** for every frame AND
for the C1 face frames, make an image of the face crop next to the same character's face from the reference sheet
(`references/characters/*.png` in the main checkout or the Pages link) and compare hair color/brightness (Jimmy =
bright orange-ginger springy curls, Ava = warm medium brown), curl shape, face shape and eye size. Darker, flatter,
older or more doll-like = regenerate. Attach the character sheets to every frame edit too (not only the hook frame),
prefer the HOME outfits shown on the sheets, and ask for soft even daylight with true colors (no golden-hour tint).
**FACE DESIGN (her 2nd note, 1 Nov: "the face design changed"):** paste the FACE DESIGN LOCK line from SKILL.md
section 13 into every frame prompt, put the sheets FIRST in image_urls ("image 1 = Jimmy's sheet: copy his face design
exactly"), and judge the side-by-side on eye size, pupil size, lashes, nose size and skin smoothness. The 1 Nov frames
had smaller eyes, small light pupils, no lashes on Jimmy, a bigger nose and textured freckled skin
(`assets/face_drift_2026-11-01.jpg`) – that is a fail even when every color key is right.

## 5. Animate — Seedance 1.0 Pro (Step 3)
**1 Nov 2026: `seedence-1-0-pro` is RETIRED on ViewMax** ("This video model has been retired", nothing charged). Use
`viewmax-c1`, mode `image-to-video`, resolution `768P`, aspect_ratio `9:16`, duration `10s` (20 credits per shot,
768×1344, 24 fps, ~10 min queue; it held identity well on the 1 Nov puppy short). Add "No talking, no dialogue, no music.
Silent." to the motion prompt (C1 can make voices; montage.py replaces the audio anyway). Everything below about
Seedance (motion rules, checks) applies to C1 the same way. Budget: 5 × 20 = 100 + effects.
`generate_video` model `seedence-1-0-pro`, mode `image-to-video`, image_urls = [frame URL], resolution `1080p`,
duration `10s`, idempotency_key `cb-<date>-<slug>-s<N>`. Motion prompt: identity keys in CAPS, small gentle movements,
still camera, NO hugging, turning around, covering faces, long closed-eye laughing or anything passing in front of
a face. Silent. `wait_for_task`, then `curl -sSL -o W/shotN.mp4 <url>`.

## 6. Clip check (Step 4)
`python3 montage.py faces W N 3 6 9.5` for every shot → look at the frames vs the start frame. If a shot drifted,
redo only that shot once (`-r1`, 14 credits). Never more than one redo in the whole run.
Also check STORY ORDER on the 4 fps sheets: the drawn/fixed/brought thing is absent before its moment (Seedance likes
to add a missing part on its own — and in the 30 Oct kitty short the tail was already finished in the drawing shot),
appears during it, present after. A shot that breaks the order is the redo, before any identity nit.

## 6b. NO STILL PICTURES AS SHOTS (her note, 2 Nov 2026: "why are most shots static? I didn't like it")
The 2 Nov "Count to 5" run replaced one bad C1 clip with 4 slow zoom-ins on still frames (shot6–9) and used them in
8 of 15 cuts (~17 of 30 s) – she saw a mostly frozen video. Rules:
- NEVER build a shot from a still image (no zoompan / Ken Burns on a frame). Every cut must be real C1 motion.
- If a C1 shot is unusable (wrong count, drift, story order), REDO it (that is the one allowed redo, 20 credits;
  budget up to ~125 credits for this case). If a second shot also fails, rebuild the edit from the good real clips
  (more cuts per clip, punch-ins, different moments) rather than stills.
- Motion prompts ask for clear, lively, bouncy action in every shot (clapping, bouncing, pointing, reaching, nodding,
  wiggling, objects moving), still with faces visible and no hugs/turns – "small gentle movements" alone gives
  near-frozen clips.
- Clip check: measure motion per shot (ffmpeg tblend difference, mean YAVG over the clip); below ~1.0 = too static,
  use only its liveliest seconds or redo it.

## 7. Song — Lyria clip, 30 s (section 8 style)
Write `W/song_prompt.txt`: the section 8 style (a cappella children's voices, humming and "la la", ONLY daf and hand
claps, ~110 BPM, major key, ONE child voice – a sweet little boy for Jimmy videos, a sweet little girl for Ava videos – singing solo, slowly and clearly in simple English, with soft children's humming backing).
  **NO musical instruments at all** (her firm rule, for religious reasons): only children's voices singing, humming and "la la", mouth sounds (soft beatbox, "boom-chk", tongue clicks), hand claps, finger snaps and a daf/frame drum. Write in the prompt: "NO instruments: no piano, no guitar, no ukulele, no bells, no xylophone, no synth, no strings, no flute, no electronic beats".
   + the lyrics
with timestamps so each line lands on its beat, e.g.
`[0:00 - 0:03] Hook: "Oh no! ..."` … `[0:26 - 0:30] Outro: "Bye bye, friends!"`.
Short lines, repetition, the lesson as the chorus. Then:
`python3 song.py W/song_prompt.txt W/song.mp3` (model `lyria-3-clip-preview`, exactly 30 s, about 8 US cents).
- Exit 3 = Gemini prepaid credits empty/quota → see step 2b: stop the run (never publish without a song).
- Other error: read it; if the Interactions API response shape changed, fix `song.py`, commit the fix, retry once.
- You cannot hear audio: never claim it sounds good. Check the duration and that mean_volume is not silent.
- Find where the singing starts: `ffmpeg -i W/song.mp3 -af silencedetect=n=-35dB:d=0.3 -f null -` → `song_start`.

## 8. Sound effects
Reuse `sfx/*.mp3` (see `sfx/README.md`). Generate at most 3 new ones for this story's special moments with
`generate_sound_effect` (5 credits each, idempotency keys `cb-<date>-<slug>-fx<N>`); download them into W.
Save reusable ones into `sfx/` with a row in `sfx/README.md`.

## 9. Edit plan — the approved montage (Step 5)
`python3 montage.py sheets W` → LOOK at every sheet. Then write `W/edit.json` (format in `montage.py` docstring):
- 10–14 cuts of 1.2–3.5 s, total ≈ 30 s (the song length). Hook = the strongest 1–1.5 s at `speed` 0.8–0.9 (0.65 looked like a stopped picture – 2 Nov).
  A second cut from the same shot gets `zoom` 1.10–1.12. Skip blinks, look-downs, blur, drift, extra hands.
  End on shot 5 (the loop shot).
- **NO on-screen words** (her rule, 29 Oct 2026: text like "ROAR?" / "Meow?!" looked out of place). Never set
  `show_words`; the picture, the song and the sound effects tell the story.
- Effects on the exact visual moments (mouth opens, clap, pop…) read from the sheets; character sounds vol 0.5–1.0.
`python3 montage.py build W/edit.json` → `W/final.mp4`, `W/final_sheet.jpg`, `W/final_hook.jpg`.
LOOK at both sheets (first 2 s especially, no text on screen, no bad frames, identity OK) and run
`python3 montage.py motion W/final.mp4`: every second must be ≥ 2.0 (her rule: the picture never stops) – replace the
low pieces with livelier moments, rebuild (free) and measure again. Fix edit.json and rebuild
if needed (free). Final file name for people: `Crayon Babies - <Title>.mp4`.

## 10. Title, description, tags (section 10)
English + emoji title with the hook first; description template with NO hashtags; 11–15 tags starting with
`crayon babies` + the star (`baby jimmy` or `baby ava`); playlist "Crayon Babies Songs". Write `jobs/<date>-<slug>.json`:
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
