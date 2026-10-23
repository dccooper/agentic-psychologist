# Lesson Outlines

Working outlines for every lesson after 1.1. Each becomes a full script (see `LESSON_TEMPLATE.md`) once Slice 1 testing confirms the format works. **Key moment** = the one thing the learner should walk away feeling.

Drafted: 0.1, 0.2, 1.1 (full scripts).

---

## Module 1: Foundations (continued)

### 1.2 Ask, Plan, and Agent modes (~20 min)
- **Scenario:** Dr. Okafor wants "thoughts" on fixing the shared drive (`FINAL`, `FINAL_actual`, `USE THIS ONE`).
- **Steps:** **Ask** mode: question the mess without changing anything. **Plan** mode: have the AI propose a reorganization. **Agent** mode: carry out the plan on a practice copy of the folder.
- **Key moment:** pick the mode by risk. *Read → think → act.*
- **New artifact:** `world/artifacts/shared-drive/` (about 10 small, badly named dummy files)

### 1.3 Giving the AI context with @ (~20 min)
- **Scenario:** the long, rambling department meeting transcript.
- **Steps:** first a vague request with no context. Then the same request with @-mentioned files, plus a role, a task, a format and constraints. Compare the two results.
- **Key moment:** the same question gets a much better answer when the AI has context. Introduces a simple prompt pattern: **context, task, format, constraints**.
- **New artifact:** `world/artifacts/dept-meeting-transcript.md`

### 1.4 First real tasks (~25 min)
- **Scenario:** turn the transcript into action items (with owner and date), then reply to Dr. Okafor's "Thoughts?" email.
- **Steps:** draft, then revise (shorter, warmer, more direct), then a final version they edited themselves. Optional: paste a screenshot (e.g., the Annex whiteboard) and ask about it.
- **Key moment:** don't accept the first draft. Revising is the skill.

---

## Module 2: Making it reusable

### 2.1 Templates and rules (~20 min)
- **Scenario:** they've now asked for action items in "their format" three times.
- **Steps:** save a template file. Then write their own rule (`.cursor/rules/my-style.mdc`), e.g., "plain language; action items always have owner + due date." Test it in a new chat without mentioning it.
- **Key moment:** the AI follows your preferences without being reminded.

### 2.2 Open the hood (~20 min) [S1]
- **Steps:** open `tutor.mdc`, the `/next-step` skill and `progress.md`. **Edit the tutor to talk like Groucho Marx** for one exchange, see it change, then change it back. Notice `progress.md` has been the agent's memory all along.
- **Key moment:** everything that taught you is plain text files, and you can edit them.

### 2.3 Build your first skill (~25 min)
- **Scenario:** a second transcript arrives (the clinic staff meeting).
- **Steps:** build `/meeting-to-actions` using their template and rule from 2.1 (via `/create-skill` or by hand). Run it on the new transcript, then improve it once.
- **Key moment:** *"I made the AI do my thing, the same way every time."* Template + rule + skill = a reusable pipeline.
- **New artifact:** `world/artifacts/clinic-staff-meeting.md`

### 2.4 The terminal isn't scary (~15 min)
- **Steps:** open Cursor's terminal panel. Run 2–3 harmless commands that work on Mac and Windows (`pwd`, `ls`). Then ask the agent to do something that needs a command, and **read what it wants to run before approving**.
- **Key moment:** the terminal is just typing instructions to your computer. The real skill is reading what the AI asks to run before you say yes.

**→ Choose your path:** Clinic (3A) or Lab (3B). It's recorded in `progress.md`.

---

## Module 3A: Clinic path (Daybreak Clinic)

### 3A.1 Meet the clinic director (~15 min) [S1]
- **Scenario:** Dr. Reyes's voice-memo brain dump: "website from 2017, referrals down, I forget everything."
- **Steps:** use Plan mode to scope two projects. Set up `workspace/clinic/`.
- **Key moment:** scope before you build.
- **New artifact:** `world/artifacts/reyes-voice-memo.md`

### 3A.2 Build a chief of staff (~45–60 min, may split in two)
- **What "agent" means here:** an agent = **instructions** (a rule or `AGENTS.md` describing the role) + **skills** (`/weekly-plan`, `/meeting-prep`, `/whats-slipping`) + **memory** (`projects.md`, `people.md`, `decisions.md`).
- **Steps:** build the chief of staff's "office" folder. Run a weekly plan from Dr. Reyes's to-do pile, then meeting prep for a referral-partner lunch. **Last step:** copy it and adapt it for *their own* life (school, personal projects).
- **Key moment:** an agent isn't magic. It's instructions + tools + memory, and you just built one.
- **New artifacts:** Reyes's to-do pile, calendar (fictional), referral-partner list

### 3A.3 Vibe code a clinic website (~45–60 min)
- **Steps:** turn the outdated clinic copy into a single-page site (one HTML file, no frameworks) and preview it in the browser. Loop: describe → build → look → refine (screenshots help). Ask the AI to explain the code.
- **Psychology hook:** a content check against the advertising sections of the APA Ethics Code (e.g., no client testimonials, no claims the clinic can't support), plus a basic accessibility check.
- **Stretch:** a referral one-pager generator.
- **Key moment:** you built a working website by describing it. (Publishing it comes in Graduation.)
- **New artifact:** `world/artifacts/daybreak-old-website.md`

---

## Module 3B: Lab path (Foresight Lab)

### 3B.1 Meet the lab (~15 min) [S1]
- **Scenario:** Dr. Lund's email chain ("quick lit review," "dashboard like that paper," grant due) and Dr. Bello's tour of the data folder.
- **Steps:** use Plan mode to scope the projects. Set up `workspace/lab/`.
- **Key moment:** scope before you build. Ask "what question does this answer?" first.

### 3B.2 Build a lab manager / lit-review agent (~45–60 min, may split in two)
- **Same structure as 3A.2:** instructions + skills (`/paper-summary`, `/lit-matrix`, `/weekly-lab-update`) + memory (`projects.md`, `reading-list.md`).
- **Steps:** summarize a small set of **openly licensed papers** into a literature matrix, then produce a weekly lab update. Last step: adapt it for their own research.
- **Psychology hook (critical):** **hallucinated citations.** The agent may only cite sources it was given, and the learner checks every citation. Include a planted trap where the AI is asked for "a few more references."
- **Key moment:** the AI speeds up reading but doesn't replace checking.

### 3B.3 Vibe code an analysis (~45–60 min)
- **Steps:** Dr. Bello sets a **question in advance** (in the spirit of preregistration). The learner has the AI write an analysis script on the public dataset, run it, explain each step, then build a small dashboard.
- **Psychology hook:** the AI will happily run 20 tests until one is significant. Stick to the stated question, and record what was tried.
- **Key moment:** fast analysis is only worth something if you can explain and reproduce it.
- **Language: Python**, with R on request. Rationale for learners: most technical data-science roles use Python. Installing it with the agent's help builds on 2.4.

---

## Module 4: Capstone

### 4.1 Build for your own work (open-ended)
- **Steps:** pick one real problem that doesn't involve patients. Scope it in Plan mode. Build a skill, agent or tool. Run the **go-live checklist**. Show it to a peer.
- **Go-live checklist:** what data it touches; institutional AI policy; BAA / IRB if it ever touches protected data; review-before-accept habits; who else uses it.

---

## Graduation (optional)

- **G.1 Version control with GitHub:** why it helps (unlimited undo, a history of your work, sharing). Use GitHub Desktop or Cursor's source-control panel to commit the capstone to a **private** repo.
- **G.2 Publishing with Vercel (optional):** publish the clinic website. Only publish things that were built to be public; never put keys in code.
- **G.3 Beyond:** terminal agents (Pi / Claude Code); Orca for running several agents in parallel.

---

## Open decisions

1. ~~**Lab path language (3B.3)**~~ → **Decided:** Python, R on request.
2. **Split long lessons?** 3A.2/3B.2 and 3A.3/3B.3 run 45–60 min each. Split into a and b?
3. **Lit-review sources (3B.2):** needs a small set of openly licensed papers (e.g., PLOS, CC-BY). Pick them alongside the dataset (Assumption 5).
4. **Personal adaptation in 3A.2 / 3B.2:** at the end of the lesson, or saved for the capstone?
