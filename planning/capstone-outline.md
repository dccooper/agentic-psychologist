# Capstone Outline: Module 4

*Draft for review, 2026-10-25. Lesson-level outline only; full scripts follow `lessons/LESSON_TEMPLATE.md` once this is agreed. Replaces the three-lesson sketch in `lessons/OUTLINE.md` (Module 4) if accepted.*

## Purpose

Module 4 is where the learner leaves the University of Tomorrow and makes an agent their own. They move their path agent (chief of staff or lab agent) into a folder of its own, run the go-live checklist, point it at their real (non-patient) work, then use it to scope and build one project of their choosing. Along the way the tutor steps back from guide to coach. By the end, the learner drives agents with their own unstructured words (typed or spoken), asks "what am I missing?", fixes skills by telling the agent what to change, and no longer needs the tutor. That last part is the point.

**Structure change (one line):** the old 4.1 is split into **4.1 Moving day** and **4.2 Go live**, because a move, a new window, a checklist, a rewrite and a first real run can't fit in 20 minutes, and the checklist must sit between "moved" and "first real data". A short **4.5 Show it, then what's next** gives the capstone a finish line and a home for the security check.

| # | Lesson | Time | Where the learner works | Tutor's role |
|---|---|---|---|---|
| 4.1 | Moving day: your agent gets its own folder | ~20 min | Course window, then the agent's window | Guide (last time) |
| 4.2 | Go live: make it yours, safely | ~20 min | Both | Guide, then coach |
| 4.3 | Pick your project: the idea gallery | ~20 min | Mostly the agent's window | Coach |
| 4.4 | Build it | open-ended, ~20 min chunks | The agent's window | Coach on request |
| 4.5 | Show it, then what's next | ~20 min | Both | Coach, then goodbye |

---

## Design principles for the capstone

- **The tutor fades on purpose.** 4.1 is the last fully scripted lesson (moving files is mechanical and easy to get wrong). From 4.2 on, the tutor asks questions instead of giving steps: "What do you want it to do? How will you know it worked? What will you check before you trust it?"
- **Coach, not guide.** The tutor doesn't prescribe prompts. It reviews only what the learner brings back, offers one observation at a time, and asks "Ready to move on?" rather than issuing the next command.
- **Two windows, two roles.** The course window is the coach's office. The agent's window is where the work happens, and the tutor isn't there. Say this plainly: being alone with your agent is a feature, not a bug.
- **The learner talks, the agent structures.** Brain dumps replace careful prompts. Every lesson includes at least one unstructured request (typed or spoken) and one "what am I missing?"
- **Fix by telling.** Skills and instructions are refined by describing the change to the agent, then reviewing the diff. Hand-editing is still allowed, never required.
- **Checkpoints become self-checks.** The learner says what "done" looks like before building, then checks it themselves. The tutor confirms only the safety-critical ones (data, publishing).
- **Pick up, put down is the learner's job now.** Their agent's `/wrap-up` (or `/lab-wrap-up`) writes the handoff. The tutor's `progress.md` only tracks which capstone lesson they're in.
- **Same three words.** Instructions, skills, memory. Diagnose by part, every time.
- **Data rules don't relax.** Real work is allowed; real patient or participant data still never is. The go-live checklist is the gate, and its red line is written into the agent's own `AGENTS.md`.
- **Knowledge checks are short and callback-heavy.** One per lesson, tied to an earlier concept, with an expected answer for the free model.

---

## Lessons

### 4.1 Moving day: your agent gets its own folder (~20 min)
- **Scenario:** the agent packs up and leaves the University of Tomorrow. This delivers the promise from 3A.2a/3B.2a: its instructions become its own folder's `AGENTS.md`.
- **Steps:**
  1. **The packing list (course window).** The learner names what moves, by part. *Instructions:* `instructions.md` becomes `AGENTS.md`. *Memory:* the `memory/` folder, which gets reset. *Skills:* their three skills (`weekly-plan`, `meeting-prep`, `wrap-up`, or `lit-matrix`, `weekly-lab-update`, `lab-wrap-up`) go into the new folder's `.agents/skills/`. Outputs (`plans/`, `prep/`, `lit-matrix.md`) stay behind as souvenirs.
  2. **Make the new home.** A folder **outside** the course folder (e.g., `Documents/my-agent`; the name is theirs). The learner asks the tutor to copy the files; the tutor explains the copy command before running it (2.4 habit). **Copy, not move**, so the course still works. Fallback: File Explorer or Finder.
  3. **Rename and reset.** `instructions.md` → `AGENTS.md`. Memory files keep their headings but lose the Dr. Reyes / Dr. Lund contents. `handoff.md` says "First session in the new home. Nothing yet." No real content goes in yet: that waits for the checklist in 4.2.
  4. **Before you go.** The tutor saves `progress.md` ("4.1, step 6: back from your agent's window") and says exactly how to return: switch back to this window and type `/next-step`. **Pause point.**
  5. **Open the new folder in a new window** (**File → New Window**, then **Open Folder** ⚠️). Accept the trust prompt. One line: *"The tutor won't be in that window. It's just you and your agent. That's on purpose."*
  6. **First conversation, alone.** The learner asks their agent, in plain words, to read its files and say who it is and what it can do. Then the first **fix by telling**: the skills still say "read `workspace/.../instructions.md`" and save to `workspace/...` paths. They tell the agent to fix the paths and drop the "read instructions first" step (its `AGENTS.md` is now always on), and to add a small command table to `AGENTS.md` mapping each `/command` to its skill file (the same backstop the course uses). They review the diffs.
  7. **Back in the course window:** `/next-step`. Short debrief: what worked, what was odd.
- **Key moment:** you moved all three parts by hand and it still works. The University of Tomorrow was practice; this agent lives in its own house now.
- **Expected learner outputs:** `<agent-folder>/AGENTS.md` (with command table), `<agent-folder>/memory/` (reset: `projects.md`, `people.md` or `reading-list.md`, `handoff.md`), `<agent-folder>/.agents/skills/<three skills>/SKILL.md` with corrected paths. Course copy untouched.
- **Knowledge check:** *"Why did your skills no longer need a 'read instructions.md first' step?"* Expected: in its own folder, `AGENTS.md` is read automatically every time (always-on instructions, as the tutor's was in 2.2).

### 4.2 Go live: make it yours, safely (~20 min)
- **Scenario:** before any real work goes in, the go-live checklist. Then the agent gets rewritten for the learner's real life, by voice.
- **Steps:**
  1. **The go-live checklist (course window, tutor confirms each item).** The learner fills `workspace/capstone/go-live.md` from a shipped template (`lessons/4-capstone/go-live-checklist.md`):
     - **What data will this touch?** List it (calendar, to-dos, reading notes, colleagues' names).
     - **Where does it go?** Prompts and attached files go to Google's models. Check Antigravity's data-use setting ⚠️ (setup defaults it on). Is the agent folder inside a cloud-synced folder (OneDrive, iCloud, Dropbox)? Then it goes there too.
     - **Institutional AI policy.** Find your school's or employer's policy. Does it allow this tool for this work? Write the link down. "I don't know" is an answer that means "ask first".
     - **Protected data.** PHI or identifiable research data: **stop**. That needs a BAA, IRB approval, or an approved tool (possibly a local model), decided with your institution. Not this setup, not improvised.
     - **Review-before-accept.** Review stays on. Name what you'll look at closely (anything that changes your real files) and what you'll glance at (bookkeeping), as in 1.2.
     - **The red line.** One or two sentences the agent must never cross (e.g., "no client names, initials, or details, ever; clinical time is written as 'clinical block'").
  2. **Rewrite the instructions with a brain dump (agent's window).** Typed or spoken ⚠️ (microphone): who I am, what I juggle, how I like things, what you must never do. The agent turns it into a new `AGENTS.md`, with the red line pasted in from the checklist. Then the learner asks: *"What am I missing?"* They accept, reject, or edit its suggestions. **Pause point.**
  3. **First real run.** One skill on real, non-patient material (their actual week, or two papers they're reading). **Clinicians:** type the week in by hand with clinical time as "clinical block". Never paste a calendar export that holds client names.
  4. **Refine a skill by telling.** Something about the output won't be quite right. They tell the agent what to change in the skill ("shorter, and always put the personal stuff last"), review the `SKILL.md` diff, and rerun.
  5. **Wrap up** with their agent's `/wrap-up` or `/lab-wrap-up`, then `/next-step` in the course window. The tutor asks two coaching questions: what surprised you, and what would you not trust it with yet?
- **Key moment:** you didn't write a careful prompt. You talked, and it organized. You're the one who knows what good looks like.
- **Expected learner outputs:** `workspace/capstone/go-live.md` (every item answered), a rewritten `<agent-folder>/AGENTS.md` with the red line, one real output (e.g., `plans/<week>.md`), one edited `SKILL.md`, a fresh `memory/handoff.md`.
- **Knowledge check:** *"Your real calendar export has client names on it. Can you attach it if you delete the names first?"* Expected: no. Removing names doesn't make data safe (0.2), and it's a red-line item. Type the week in by hand.

### 4.3 Pick your project: the idea gallery (~20 min)
- **Scenario:** the learner has a working agent. Now they choose one thing to build with it.
- **Steps:**
  1. **Browse** `lessons/4-capstone/idea-gallery.md` (same table as below; also on the site). Pick one, mash two together, or invent one.
  2. **Brain dump to your own agent (agent's window).** No template from the tutor. The learner says what they want, out loud or typed, and asks their agent to turn it into a brief: the question it answers (3A.1/3B.1), what a 20-minute first version looks like, which parts it needs (instructions, skills, memory), and what data it touches. Then: *"What am I missing?"*
  3. **Taste before building.** The learner gathers two or three examples of good: URLs, screenshots, documents or handouts they admire. They save them to `taste/` and ask the agent what makes them good. They correct it. *Why:* the agent can build anything; only you know what good looks like.
  4. **Decide where it lives.** A new skill for their agent lives in the agent's folder. A website, app or anything that might go public gets its own folder, so public files never sit next to private memory (sets up 4.5 and G.2).
  5. **Coach check (course window, optional but offered).** The learner brings back the brief's data line only; the tutor checks it against their go-live checklist and flags anything near the line (the ⚠️ practicum-hours example). "Ready to move on?"
- **Key moment:** "I could actually build that." And they scoped it themselves.
- **Expected learner outputs:** `<project>/project-brief.md` (question, first version, parts, data), `<project>/taste/` (2–3 examples plus the agent's notes, corrected), an updated `go-live.md` if the project touches new data.
- **Knowledge check:** *"Your brief needs three new things: a list of your CE credits, a procedure for checking deadlines, and a tone. Which part is each?"* Expected: memory, skill, instructions.

### 4.4 Build it (open-ended, in ~20 min chunks)
- **Scenario:** the learner builds in their agent's window. The tutor isn't watching.
- **Steps (each chunk):** pick up (the agent reads its handoff) → build one thing → look → refine by telling → `/wrap-up`. Plain language throughout; screenshots for visual work (3A.3b habit).
- **When stuck, in this order:** ask the agent ("explain what you just did", "what am I missing?"); diagnose by part (forgets → memory, inconsistent → skill, ignores preferences → instructions); then `/im-stuck` in the course window, bringing the handoff note.
- **Optional coach check-in:** `/next-step` in the course window between chunks. The tutor asks three questions (what did you build, what surprised you, what will you check before you trust it?) and gives one observation. It doesn't hand out the next step.
- **Done when:** the first version works and the learner has used it once for real. `progress.md` records the chunk count and their own one-line status.
- **Key moment:** you can stop for a week, come back, and your agent knows where you were. You built that.
- **Expected learner outputs:** the project's files, a current `memory/handoff.md`, one line per chunk in `workspace/capstone/build-log.md` (date, what got done; written by the learner or pasted from the handoff).
- **Knowledge check:** *"You come back after a week and the agent has no idea what you did last time. Which part failed, and where do you look first?"* Expected: memory. Check `memory/handoff.md`; likely `/wrap-up` wasn't run, or the skill doesn't read `handoff.md`.

### 4.5 Show it, then what's next (~20 min)
- **Scenario:** a thing that works deserves an audience. Then the course ends.
- **Steps:**
  1. **Show it to someone** (a peer, supervisor, labmate; a two-minute demo). Ask them: "What would you want it to do?" Turn one piece of feedback into a change by telling the agent.
  2. **Security before anything goes on the web.** Publishing is G.2, but the check happens now, on the project's own folder (never the agent's folder). The learner asks the agent to audit it, then checks the list themselves: no passwords, API keys or tokens anywhere; no memory files, handoff notes, `AGENTS.md`, or `.agents/` in a public folder; no personal details they wouldn't put on a flyer; no patient or participant data, ever; nothing loaded from a site they don't recognize. **Pause point.**
  3. **The retrospective** (`workspace/capstone/retrospective.md`, the learner's words): what I'd trust an agent with, what I wouldn't, and what I'll build next. (Doubles as the educator-guide assignment.)
  4. **Goodbye from the tutor.** It marks the course complete in `progress.md` and points to Graduation (G.1: put the capstone in a **private** repo; G.2: publish only what's built to be public).
- **Key moment:** you don't need the tutor anymore. You have an agent, a habit of checking, and your own way of working with both.
- **Expected learner outputs:** one feedback-driven change, a completed security check (in `go-live.md`, new section "Before anything goes public"), `retrospective.md`, course marked complete.
- **Knowledge check:** *"Name two things that must never be in a folder you publish."* Expected (any two): passwords/API keys; memory or handoff files; patient or participant data; the agent's `AGENTS.md` or `.agents/`.

---

## Idea gallery (revised)

No patient data in any of these. **Candidate** = proposed, not yet agreed.

| For | Idea | Builds on |
|---|---|---|
| Clinicians | **Psychoeducation handout generator** (topic + reading level → handout) | Skills, templates |
| Clinicians | **CE credit and license-renewal tracker** | Agent + memory |
| Clinicians | **Practice website or referral one-pager** | 3A.3 |
| Clinicians | **Workshop / talk prep agent** | Agent + skills |
| Clinicians | **Supervision prep agent** (agenda, readings, *no case details*) | Agent + memory |
| Researchers | **Weekly literature digest** from papers you drop in a folder | 3B.2 |
| Researchers | **Grant timeline and task agent** | Agent + memory |
| Researchers | **Codebook / data dictionary builder** for public or approved data | 3B.3 |
| Researchers | **Lab onboarding guide** for new RAs | Templates, skills |
| Researchers | *Candidate:* **Papers in LaTeX** (write in Markdown; the agent builds and iterates the LaTeX and PDF) | 3B.3a install, 3B.2a citation check |
| Trainees | **Comps / EPPP study buddy** that quizzes you from your notes | Skills |
| Trainees | **Internship application tracker** + essay feedback | Agent + memory |
| Trainees | **Dissertation planner** with handoff notes | Pick up, put down |
| Anyone | **Personal chief of staff** (from 4.1) | 3A.2 |
| Anyone | *Candidate:* **Tech support agent** (printer settings, a spreadsheet formula, an error message you don't understand) | 1.2 read → think → act, 3B.3a five questions |
| Anyone | *Candidate:* **Taste board** (collect examples of good, have the agent describe the pattern, reuse it as instructions) | 4.3 step 3 |

⚠️ Watch: some ideas sit near the line (e.g., practicum hour logs often include client initials; a "tech support" request may involve a work laptop with patient records on it). The tutor flags these during 4.3 scoping.

---

## Candidate side lessons

Proposed as unnumbered **Extras** (see open question 5). Both are optional and skippable.

**Extra: Your agent as tech support (~15 min). Candidate.** Slot: available any time after 2.4 (needs the terminal), suggested after 4.2.
- Scenario: a real annoyance (a spreadsheet formula, a printer setting, a cryptic error). Paste the error text or a screenshot; ask the agent to explain before it fixes anything.
- Teaches read → think → act (1.2) on your own computer: diagnose read-only first, then the five questions (3B.3a) before any command or settings change.
- Red lines: never on a machine or account that holds patient data without IT's OK; never paste passwords; "I'll call IT" is a valid answer.

**Extra: Papers in LaTeX via an agent (~25 min). Candidate.** Slot: after 3B.3a for lab learners, or as a 4.4 project.
- Write in Markdown; the agent converts it to LaTeX (e.g., the `apa7` class), compiles, and iterates on layout when you tell it what's wrong. Builds on 3B.3a's install teaching moment.
- Requirements: a LaTeX distribution (TeX Live, MiKTeX, or MacTeX; large, gigabytes) installed with the agent and the five questions, or **Overleaf** as the no-install route (paste the `.tex`; free-plan limits ⚠️). Pandoc is an optional converter.
- Psychology hook: every BibTeX entry must be a real paper you've read (the 3B.2a citation trap, again).

---

## Open questions for the author

1. **Where should the agent's folder live?** *Recommend:* outside the course folder (e.g., `Documents/my-agent`), and not in a cloud-synced folder unless the go-live checklist says that's allowed. Inside the course folder risks the tutor's `AGENTS.md` mixing in ⚠️, and a fresh course ZIP could overwrite it.
2. **Learners who finished both paths: which agent moves?** *Recommend:* pick one in 4.1. The second can move later on their own using the same packing list (a good unscripted test of what they learned).
3. **Five lessons instead of three?** *Recommend:* yes (split 4.1, add 4.5), for the reasons in the structure note. Total scripted time stays around 80 minutes plus the open-ended build.
4. **A new course command for coach check-ins, or reuse `/next-step`?** *Recommend:* reuse `/next-step` (and `/im-stuck`). The `/` menu stays small, and the lesson scripts switch the tutor into coach mode.
5. **Numbering for side lessons.** *Recommend:* unnumbered **Extras** listed after Module 4 in `lessons/README.md` (e.g., `extras/tech-support.md`), so they never interrupt the 4.x sequence and can be offered at any point after their prerequisite.
6. **Should the tutor see the agent's folder at all?** *Recommend:* no. The learner brings back what's needed (the handoff note, the brief's data line). It keeps the coach's role honest, and the agent may not be able to read outside its window anyway ⚠️.

---

## ⚠️ Things to verify in Antigravity

- **New window and Open Folder:** exact menu labels (**File → New Window**, **Open Folder**), whether Open Folder replaces the current window unless a new one is opened first, and the trust prompt's wording in a second folder.
- **`AGENTS.md` in the new folder** is read as always-on, with no extra setup.
- **Nesting:** if a learner puts the agent folder inside the course folder, does the course's `AGENTS.md` (or `.agents/rules/`) also apply? Decides how firmly to warn in 4.1.
- **Skills in a new folder:** `.agents/skills/` is found, `/` shows them, and Tab completion works, in a window that has never seen the course.
- **Global rules or skills:** does Antigravity have user-level rules or skills (e.g., in the home folder) that would carry across windows? Make sure the course installs nothing global, and decide whether to mention them as a later option.
- **File access outside the workspace:** can the agent in the course window copy into a folder outside it (file tools vs. a terminal command)? Decides step 2 of 4.1 and the fallback.
- **Conversations per window:** does the new window show the old course conversations? Is the Free weekly limit shared across windows (presumably yes, per account)?
- **Data-use setting:** where it lives and how to turn it off, for the go-live checklist. Wording of what Google says it does with interactions.
- **Microphone / dictation** in the agent panel, Windows and Mac permission prompts (already open in `SCREEN_GUIDE.md`).
- **Pasting or attaching screenshots** in the agent panel (taste examples, tech support).
- **Switching between two Antigravity windows** reliably on Windows and Mac (the learner must find their way back to the course window).
- **LaTeX extra:** whether a TeX install through `winget` works from Antigravity's terminal, and Overleaf's current free-plan compile limits.
