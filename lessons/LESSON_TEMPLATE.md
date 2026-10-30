# Lesson X.Y: Title

<!-- Lesson scripts are read by the professor agent, not the learner directly. Write them as instructions to the professor. -->

- **Module:** X (shared | clinic | lab)
- **Time:** ~N min
- **Request budget:** ~N agent requests (update from free-tier testing)
- **Last tested:** Antigravity IDE X.Y on YYYY-MM-DD

## Goal

What the learner can do after this lesson, in one sentence, in their own terms.

## Why it matters to a psychologist

One or two sentences tying this to real clinical or research work.

## Setup

Files from `world/` or `data/` this lesson uses. Anything the professor should check first.

## UI this lesson depends on

Every on-screen control the lesson uses (by label), pointing to `lessons/SCREEN_GUIDE.md`. This list is the regression checklist: when Antigravity updates, recheck these. Lead with labels; position is only a hint.

## Steps

1. **Step name:** what the learner does. *Why:* one line.
   - ✅ **Checkpoint:** how the professor confirms it's done (a file exists, the learner reports X). If the answer is a fact from a file, write the **expected answer** here so the professor doesn't have to guess.
2. ...

Also in every lesson:
- Somewhere in the lesson: **one quick knowledge check** that recalls an earlier idea (with the expected answer).
- When the learner creates a skill, rule, or instructions file: prompt them to ask the AI *"Is anything missing?"*
- When a new skill is created: run it in a **new conversation** (it isn't available in the one that created it).

N. **Name the moment:** one or two sentences, said *after* the exercise, naming the skill they just practiced and how it carries over to real work.

## Pause points

**At most one** mid-lesson stop (e.g., "after step 3"), plus the end of the lesson. At each one, the professor briefly offers a break and updates `progress.md` so `/start-course` resumes exactly here. Between other steps the professor just asks "Ready to move on?" (QA pass 4: lessons run faster than planned).

## Done when

The final checkpoint(s) that complete the lesson.

## Common sticking points

- Symptom → hint to give.

## Avoid

- Things the professor must not do in this lesson (e.g., don't introduce the terminal yet).
