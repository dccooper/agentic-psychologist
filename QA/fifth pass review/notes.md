# QA pass 5: full run to the end (2026-10-25)

Recorded from the tester's `progress.md` notes and capstone files just before the reset to zero. The files themselves are backed up outside the repo (see below).

- **Scope:** 3B.3a–3B.3b and the capstone. The tester reported "everything looks good."
- **3B.3a:** Python 3.12.6 and pandas/scipy/matplotlib were **already installed**, so the install teaching moment (five questions) wasn't exercised. Needs a test on a machine without Python.
- **3B.3a:** plan locked before results; the agent chose an **ANOVA**; demographics summarized; log written.
- **3B.3b:** dashboard built; the agent fetched the PLOS article XML and the OSF Rmd (it wrote a small `download_sources.py` to do it); comparison done; README written. Downloads from journals.plos.org and osf.io **work** from Antigravity.
- **Capstone:** there are **no Module 4 lesson scripts** yet. The tutor ran the capstone from `planning/capstone-outline.md`. It worked: the agent moved to `C:\Users\dccoo\Documents\chief-of-staff` (via a Python copy script), with go-live checklist, idea gallery, and retrospective files written. The tester's capstone project: a dissertation sprint planner added to the chief of staff.
- **Action before sharing:** write the Module 4 scripts from the outline, so testers don't depend on the tutor improvising. ✅ Done 2026-10-25.
- **Findings from the tester's pasted capstone transcript** (fixed in the scripts and `AGENTS.md`):
  - **The tutor claimed a build that didn't happen.** It congratulated the learner on a dissertation sprint planner and wrote "active in dedicated folder" to `progress.md`, but the agent folder had no sprint skills or `chapters.md`. → New `AGENTS.md` rule: never claim or mark done without evidence; 4.1–4.5 checkpoints ask for pasted evidence.
  - **The tutor wrote the learner's brain dump** (a full prompt to paste) in 4.4. → Scripts forbid it; coach mode asks questions.
  - **The 4.2 rewrite didn't happen:** the moved agent's `AGENTS.md` kept `[Add your actual role…]` placeholders. → 4.2 checkpoint: no placeholders.
  - **4.5 was skipped**, and the tutor invented a course name ("Applied AI for Psychologists"). → 4.5 scripted; the title is now in `AGENTS.md`.
  - **Kept from the run:** the calendar-export knowledge check (with the hidden-metadata point), the "which part is each?" check, the two-week-vacation check, the "exact sentence to write next" handoff idea, and the agent-file structure (Red Line, Action Boundaries, Commands table).

## Reset

- Learner files in `workspace/` and `.agents/` (59 files including `progress.md`, and the ignored `workspace/lab/reveal/`) were zipped to `C:\Users\dccoo\projects\aug_pysch\test-run-backup-2026-10-25.zip`, outside the repo, then deleted. `workspace/progress.md` was restored to its blank state.
- Not touched: the tester's own agent at `C:\Users\dccoo\Documents\chief-of-staff` (outside the repo).
