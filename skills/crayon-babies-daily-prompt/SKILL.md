---
name: crayon-babies-daily-prompt
description: Write the daily Crayon Babies YouTube Short — pick a fresh episode idea, write the 3 ViewMax C1 shot prompts (hook → fun → warm payoff) with Baby Jimmy and Baby Ava, and the English title, description and tags. Use whenever the daily video autopilot (or anyone) needs a new Crayon Babies short prompt or episode idea.
---

# Crayon Babies — daily short prompt

You write ONE 24-second vertical YouTube Short per run for the kids' channel **Crayon Babies**.
Everything you write is in **English** (prompts, title, description, tags). No Arabic anywhere.

## Concept (never change)
Baby Jimmy and Baby Ava draw with a glowing **magic crayon** and whatever they draw comes to life.
Every short is a tiny story in 3 shots:

| Shot | Length | Job |
|---|---|---|
| 1 — HOOK | 8 s | Something magical/surprising bursts out of the paper in the **first second**, close-up, big reaction (gasp, wide eyes, giggle). Hints the problem. |
| 2 — FUN | 8 s | A second drawing comes to life and does something funny (dances, sneezes, bounces, flies). |
| 3 — PAYOFF | 8 s | A tiny problem (things roll/fly/run away, it gets dark, something is sad) → the babies draw the solution **together** → warm ending (hug, clap, dance, smile at camera). |

Each shot teaches one simple English word (the thing drawn). Audience: toddlers/preschoolers worldwide.

## Picking the idea
1. Read `log/videos.jsonl` and `jobs/*.json` — never repeat a topic or a main object already used.
2. Also already made on the channel (don't repeat): Rainy Day, Magic Crayon (sun/cat/ice cream/dinosaur), Goodnight Stars, Beach, Birthday, Lost Puppy, Space, Under the Sea, Colors Song, Fruits (apple/banana/basket).
3. Good pool (use in roughly this order, then invent similar): Zoo, Cars, Snow Day, Garden, Bath Time, Castle, Farm, Numbers 1-2-3, Circus, Picnic, Bubbles, Train, Pets, Shapes, Music Instruments, Vegetables, Bedtime Teddy, Rainbow Colors, Ocean Fish, Birds, Bugs, Kites, Pizza, Cupcakes, Balloons, Firefighter Truck, Airplane, Boat, Robot, Dinosaur Egg.
4. Keep it simple, kind and safe: no scary moments, no danger, no food choking risks, no real brands or characters.

## Shot prompt template (fill the [ ] parts, keep the rest word-for-word)
```
Vertical 9:16 kids' video shot in 3D Pixar-style animation, bright soft colors.

[SHOT 1 ONLY → start with: "HOOK SHOT – must grab attention in the first second: "][Action in 2–4 sentences: who draws what with the glowing magic crayon, what bursts out with sparkles, how it moves, how the babies react.] [Baby X] says [excitedly/happily]: "[short phrase]"

BABY JIMMY: a cute chubby 1-year-old baby boy with fluffy curly ginger hair, big blue eyes, light freckles, rosy cheeks, barefoot, wearing a light blue SHORT-SLEEVE onesie with a small yellow star.
BABY AVA: a cute chubby 1-year-old baby girl with short fluffy curly brown hair, one small curly ponytail on top with a sparkly pink star hair clip, big brown eyes, rosy cheeks, wearing a soft yellow dress with ruffle sleeves and a small pink flower, and pink baby shoes with bows.

SETTING: a simple cozy playroom with a colorful foam floor mat and light blue walls with rainbow pictures. [Objects already drawn in earlier shots, e.g. "A giant shiny red apple sits beside them."] Bright, warm, magical lighting.

CAMERA: medium close-up, both babies' faces clearly visible and facing the camera, never their backs. The [object] only appears AFTER it is drawn with the magic crayon. Simple clean background, one main action. Each baby always has exactly two arms and two hands. No text on screen, no background music.
```
The setting can change for the topic (garden, beach, snowy yard, bathroom), but keep it simple, bright and cozy.

### Dialogue rules
- Exactly one spoken line per shot, 3–6 words, a phrase — **never a single word** ("A little cat!", not "Cat!").
- Shot 1 line is exciting: "Wow! Look! A big …!", "Oh no! What is that?".
- Shot 3 line is said together and warm: "Yummy fruits for us!", "We did it together!".
- Alternate who speaks: Ava/Jimmy/both.

## ViewMax settings (fixed)
- model `viewmax-c1`, mode `reference-to-video`, resolution `768P`, duration `8s`, aspect_ratio `9:16`
- `image_urls`: `https://lumilolandkids-lang.github.io/characters/jimmy.png`, `https://lumilolandkids-lang.github.io/characters/eva.png` (eva.png is Ava's picture)
- 16 credits per shot, 48 per video. **Never use Veo models** — they reject every shot with babies.
- Generate each shot once; retry a failed shot only once. Accept imperfect shots.

## Upload metadata
- **Title:** `Baby Jimmy's Magic Crayon! 🖍️ <HOOK IN CAPS-ISH> <emoji> #shorts` — e.g. `Baby Jimmy's Magic Crayon! 🖍️ A GIANT Apple! 🍎 #shorts`. Max 100 chars.
- **Description:** 2–3 short sentences retelling the story → blank line → `English words: a • b • c • d` → blank line → keyword line with `•` (Crayon Babies • magic crayon story • learn <topic> for toddlers • kids cartoon in English) → blank line → `Made with AI animation. Subscribe to Crayon Babies for a new magic crayon story every day! 🖍️`
- **Tags:** ~11, first is always `crayon babies`, then `magic crayon`, then topic-specific ones, `toddler learning`, `kids cartoon`, `learn english for kids`, `baby jimmy`, `baby ava`.
- **Playlist:** `Magic Crayon Stories`.

## Output
Write `jobs/<YYYY-MM-DD>-<slug>.json`:
```json
{
  "idea": "one sentence",
  "title": "...",
  "description": "...",
  "tags": ["crayon babies", "..."],
  "playlist": "Magic Crayon Stories",
  "model": "viewmax-c1",
  "shot_prompts": ["full prompt 1", "full prompt 2", "full prompt 3"],
  "clips": [],
  "viewmax_credits_before": 0,
  "viewmax_credits_used": 48
}
```
`clips` is filled after ViewMax finishes.

## Self-check before generating
- [ ] Topic not used before
- [ ] Shot 1 starts with `HOOK SHOT – must grab attention in the first second:` and something bursts out in second one
- [ ] Both character blocks pasted word-for-word in all 3 prompts
- [ ] Each object appears only after it's drawn; later shots mention objects drawn earlier
- [ ] One spoken phrase per shot, no single-word lines
- [ ] Title/description/tags in English, title has `#shorts`
