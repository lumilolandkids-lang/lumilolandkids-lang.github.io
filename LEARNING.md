# Crayon Babies — LEARNING DESIGN (her request, 31 Oct 2026)

"I want the coming videos to be important, educational and fun — I want my channel to be very special."
Audience: toddlers and preschoolers (1–5). EVERY video = ONE concrete learning goal + 2–3 fun mechanics.
A video that is only cute, with nothing a child can learn, copy or answer, is not good enough.

## 1. Weekly learning calendar (New York weekday; slot 1 = morning run, slot 2 = afternoon run)

| Day | Slot 1 – school readiness | Slot 2 – life skills & values |
|---|---|---|
| Mon | Numbers & counting (1–10 in order, then 1–20) | Healthy habits (wash hands, brush teeth, veggies, water, sleep) |
| Tue | Colors & shapes | Feelings & kindness (sharing, sorry, please/thank you, helping, taking turns) |
| Wed | Animals & their sounds / nature | Safety (hold hands crossing, hot stove, stay close, seatbelt, no climbing) |
| Thu | Letters & first words (A–Z in order, one letter + its sound + 2 words per short) | Routines & independence (getting dressed, tidy up, bath, bedtime, shoes on) |
| Fri | Body parts & opposites (big/small, up/down, hot/cold, fast/slow) | Family & friends (Mommy Lily, Daddy Tom, Leo, Mia, Biscuit) |
| Sat | "What's Missing?" signature episode (observation + vocabulary) | Little science wonder (rain, shadows, seeds grow, float/sink, magnets, melting ice) |
| Sun | Review song: the week's best learning word in a NEW story | Seasonal / holiday / special-day story |

- Series move forward: read `log/videos.jsonl` and continue where the last episode stopped (next number, next letter).
- Seasonal days (Halloween, first snow, Christmas, Eid, spring, back to school) may replace slot 2 – keep a learning goal.
- Weekly music video (Friday): a full LEARNING SONG – counting 1–10, colors, ABC part, animal sounds, body parts,
  days of the week, clean-up, brush your teeth, feelings… one theme, many repetitions.

## 2. Fun mechanics (use 2–3 in every video)
- **Interactive pause:** a character asks the viewer ("How many apples?", "What color is it?", "What's missing?") →
  1.5–2 s pause with a curious "hmm?" sound → the answer, celebrated.
- **Say it with me:** the target word sung at least 3 times; the chorus IS the lesson.
- **Copy-me action** kids can do at home: clap, jump, wave, touch your nose, count on fingers, stretch tall.
- **Surprise & payoff:** magic crayon reveal, a funny gentle mistake (Biscuit runs off with the sock), a big happy
  celebration with a cheer sound.
- **Signature touches:** "Magic crayon, draw with me!" + sparkle chime, the loop ending, "Bye bye, friends!".

## 3. Learning checks — write them in plan.json → "learning" and tick them before spending credits
- `goal`: one sentence ("Count 1 to 5 apples").
- `target_words`: 2–4 simple English words.
- `shown_how`: how the picture shows it (5 red apples in a clear row; a big yellow sun).
- `song_repeats`: where the words repeat in the timestamped lyrics (≥ 3 times).
- `interactive_moment`: the timestamp of the question + pause.
- `fact_check`: numbers, colors, shapes, letters and animal sounds exactly right. Object COUNTS on screen must match
  the number sung – image models often add or drop items, so ask for the exact number "arranged clearly in a row,
  easy to count" and COUNT them in the frame check (Step 4). Wrong count → regenerate the frame (free).
- `modeling`: the characters model the right behavior; any wrong choice is gently corrected in the same video.
- `toddler_fit`: simple words, bright but calm pacing, nothing scary, faces big.

Title and description show the learning goal: e.g. "Count to 5 with Jimmy! 🍎 | Learn Numbers | Crayon Babies",
"📚 Kids learn: counting 1–5 • apple • five".
