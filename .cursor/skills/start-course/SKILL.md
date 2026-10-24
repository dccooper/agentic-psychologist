---
name: start-course
description: Begin or resume the course. Use when the learner types /start-course or says they want to start.
---

# Start the course

0. **Check that you can edit files.** If this chat is in **Ask** mode (read-only), don't start the lesson. Say: *"Before we start: I need to be able to save your progress. In the message box, click the × on the **Ask** tag, then type `/start-course` again."* Then stop.
1. Read `workspace/progress.md`.
2. **If no lessons are marked complete:** welcome the learner warmly in 3–4 sentences:
   - They're a new trainee arriving at a fictional university psychology department (see `world/department.md`).
   - The course teaches by doing. They'll type, click, and build things themselves, and you'll guide them.
   - Nothing here uses real patient or participant data, ever.
   - They can type `/next-step`, `/im-stuck`, or `/my-progress` at any time.

   Then set the current lesson to the first lesson in `lessons/0-getting-started/` and begin it by following its script.
3. **If they've already started:** welcome them back in one sentence, say which lesson they're on (from `progress.md`), and pick up at the next unfinished checkpoint.
4. Update `workspace/progress.md` (current lesson, last session date).
