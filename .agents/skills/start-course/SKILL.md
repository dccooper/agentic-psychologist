---
name: start-course
description: Begin or resume the course. Use when the learner types /start-course or says they want to start.
---

# Start the course

0. **Check that you can edit files.** If you can't (for example, file editing is turned off or every edit is blocked), don't start the lesson. Say once, plainly, that you need to be able to save their progress, and help them fix it using `lessons/SCREEN_GUIDE.md`. Then stop.
1. Read `workspace/progress.md` with your file tools. **Don't run terminal commands to check anything** (no `git status`, no `ls`). Reading files is enough, and a command prompt this early would worry a new learner. See `AGENTS.md` → Running commands.
2. **If no lessons are marked complete:** welcome the learner warmly in 3–4 sentences:
   - They're a new student arriving at a fictional university psychology department (see `world/department.md`).
   - The course teaches by doing. They'll type, click, and build things themselves, and you'll guide them.
   - Nothing here uses real patient or participant data, ever.
   - They can type `/next-step`, `/im-stuck`, or `/my-progress` at any time. (Typing the first few letters and pressing **Tab** fills in the rest.)
   - **Your replies can take a minute or two.** While you work, the agent panel shows *Working…* or what you're reading. Tell them to wait rather than refresh or resend.

   Then set the current lesson to the first lesson in `lessons/0-getting-started/` and begin it by following its script.
3. **If they've already started:** welcome them back in one sentence, say which lesson they're on (from `progress.md`), and pick up at the next unfinished checkpoint. **Catch-up check:** compare the completed lessons with the order in `lessons/README.md`. If an earlier lesson now has a script in `lessons/` but isn't marked complete (it was skipped while still being written), tell them in one sentence and offer to do it now or carry on. Don't edit `progress.md` just to record the visit. Save the session date the next time you save anyway.
4. For a brand-new learner, `progress.md` is first written in Lesson 0.1, step 1 (their name).
