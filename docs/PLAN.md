# Repo Plan: An AI-Tools On-Ramp for Psychologists

*Working title TBD (see Assumption 7). Modeled on [Cursor for PMs](https://cursorforpms.com/): a course you learn **inside** the tool, not from a website.*

Status: plan, produced from a grilling session on 2026-10-21. Nothing built yet.

---

## 1. What this is

A free, open, downloadable course that teaches psychologists to use an AI coding agent (Cursor) by doing real work inside it. Learners go from "I've never opened an editor" to building their own reusable skills, an agent, and a small vibe-coded project, then take a first step toward common agentic-development practice (GitHub).

## 2. Audience and core problem

**Audience:** Psychology trainees, plus curious clinicians and researchers, who are new to AI tools.

**Core problem:** Fear and not knowing where to start, not missing features. The questions this course answers:
- What would I even use this for?
- Where do I start?
- The command line looks scary. Do I have to?

**Not a goal:** Getting AI tools adopted at an institution. This is an on-ramp, not an implementation program.

## 3. Tool

**Cursor for v1.** It has a graphical editor, a chat pane and a file tree, so learners don't start in a terminal. The Cursor for PMs format has already proven it works there.

- **Pi / Claude Code** (terminal agents) and **Orca** (running several agents in parallel, git-worktree based) were considered. Orca puts agents in terminal panes and assumes git plus an existing agent subscription, so it's a poor start for beginners. Both are candidates for **Graduation**, not v1.

### 3.1 Cost: keep the bar as low as possible

Cursor pricing as checked on 2026-10-21: **Free** ($0; "Limited agent requests," with no published numbers), **Plus** ($8/mo), Premium ($30/mo), and higher tiers. No standing free trial or student year is listed. Student offers are campus promotions only.

The tutor format uses requests heavily, since every exchange with the tutor is an agent request. So:

1. **Goal:** a learner on the Free plan can get from download to their first skill (end of Module 2) without paying. Ideally they can finish the whole course on Free.
2. **Lean lesson scripts:** checkpoints run in batches, the tutor doesn't chat for its own sake, and nothing is regenerated without a reason.
3. **Be honest about cost in Module 0:** "Free should get you through ___. If you hit the limit, the $8 Plus plan finishes the course." No surprise paywalls.
4. **Free-tier test protocol** (runs with every slice; see §10):
   - Testers use **brand-new Free accounts only**.
   - Record requests used per lesson (from Cursor's usage view, or the tester's notes), where the limit was hit if it was, and what happened then.
   - Keep a running `docs/free-tier-budget.md`: requests per lesson, the cumulative total, and the point where Free runs out.
   - Exit criterion for v1: Modules 0–2 fit inside Free with margin. If they don't, cut or batch lessons before considering a paid requirement.
5. **Alternatives to evaluate** (all unverified; check during Slice 1):
   - Cursor **Plus at $8/mo** as the stated fallback. Arguably an acceptable bar.
   - Cursor with **bring-your-own API key**, if the Free plan supports it. Check whether this works and what it costs per course run.
   - Institutional licenses or campus promotions (covered in the educator section).
   - A secondary target editor with its own free tier (e.g., VS Code + a free Copilot tier) is **not** in scope for v1. Only revisit it if Free plus $8 fails.

## 4. Data rules (non-negotiable)

- **No real patient or participant data, ever.** The course is synthetic or public-data only.
- **Clinic path projects avoid patient data by design:** business operations, marketing, planning and personal productivity. Any clinical-content examples are fully synthetic.
- **Lab path uses openly licensed public datasets** (CC0 / CC-BY, e.g., OSF). No datasets that require a data use agreement or forbid redistribution.
- **Module 0 includes the lesson "What never goes into an AI tool":** PHI, identifiable research data, and the myths about de-identification.
- **The tutor rule includes a guardrail:** if pasted content looks like real PHI, the tutor stops and warns. This is a nudge, not a guarantee (Assumption 4).
- **The capstone go-live checklist** covers BAA status, institutional approval, IRB, and local models if needed, before any real-world clinical or research use.

## 5. The fictional world

One shared setting: **a fictional university psychology department**, playing the role TaskFlow plays in Cursor for PMs.

- **The department:** the learner is a new trainee getting oriented. Modules 0–2 happen here.
- **The training clinic:** a small community clinic run by the department, with a director, clinicians and trainees. Setting for the clinic path.
- **The research lab:** works on a real public dataset, with a demanding PI, a grant deadline and messy data. Setting for the lab path.

Learners can try both settings. The **capstone leaves the fictional world**: build something for your own real (non-patient) work.

Content to create: `world/` docs covering the department, clinic and lab overviews, cast of characters, recurring artifacts (meeting transcripts, emails, schedules, datasets).

## 6. Curriculum

| Module | Shared / split | What the learner does | ~Time |
|---|---|---|---|
| **0. Getting started** | Shared | Install Cursor, download the course, bootstrap, arrive at the department. *What never goes into an AI tool.* Honest note about cost. | 30 min |
| **1. Foundations** | Shared | Interface, files and folders, Ask/Plan/Agent modes, @-context. First real tasks: meeting transcript → action items, rewrite an email to the director. | 1.5 h |
| **2. Making it reusable** | Shared | Rules files, templates, reusable pipelines, **first skill/command**. **Open-the-hood lesson** (§7.3). *The terminal isn't scary*: run one command on purpose. | 1 h |
| **3A. Clinic path** | Split | **Agent:** chief of staff for the clinic director (planning, project tracking, weekly review, personal-life planning too). **Vibe code:** a clinic marketing site or referral one-pager generator. | 2–3 h |
| **3B. Lab path** | Split | **Agent:** lab manager or literature-review assistant. **Vibe code:** an analysis script and small dashboard on a public dataset. | 2–3 h |
| **4. Capstone** | Shared | Build one thing for your own real, non-patient work, plus the go-live checklist. | Open-ended |
| **Graduation** | Optional | **GitHub for version control** (Cursor's built-in git or GitHub Desktop, not command-line git): a first taste of agentic-dev practice. Optional: Vercel publishing (only things built to be public; no API keys in code), terminal agents (Pi / Claude Code), Orca. | Later |

Design rules:
- The paths split **after** Module 2. Everyone builds their first skill before choosing.
- **Both paths have the same shape:** one agent build plus one vibe-code project.
- Target about 5–6 hours to the capstone.

## 7. How the course works

### 7.1 Distribution
- **One GitHub repo** holds the course files and the docs site.
- **GitHub Pages** hosts the reference and setup site (like cursorforpms.com's guides). Teaching happens in Cursor, not on the site.
- Learners get the course with **"Download ZIP"** (no git required up front). An optional one-line bootstrap prompt ("Fetch [url] and help me start…") is offered as a convenience.

### 7.2 Teaching method
- **Tutor rule** (in Cursor's project rules): the agent acts as a patient guide for psychologists. It moves one step at a time, explains why, **never does the learner's work for them**, and enforces the data guardrail.
- **Lessons as slash commands** (`/start-1-2`, `/next`, `/stuck`, …), each pointing to a lesson script in `lessons/` that says what to teach, what the learner must do, and how to check it was done.
- **Progress in files** (`progress.md` in the learner's project folder), updated by the agent, so learners can stop and resume.

### 7.3 Open the hood (decision B)
The course **works out of the box**. Learners don't build the machinery first. In Module 2 a lesson reveals: *"Everything that's been teaching you is made of the same things you're about to build."* The learner opens the tutor rule, reads a lesson command, edits the tutor's tone and watches the change take effect, notices that `progress.md` has been the agent's memory all along, then builds their own first skill from that model.

### 7.4 Proposed repo layout (verify against Assumption 1)
```
/
├── README.md                 # what this is, quick start, links to Pages site
├── LICENSE-CONTENT           # CC BY-SA 4.0
├── LICENSE-CODE              # MIT
├── .cursor/
│   ├── rules/                # tutor rule, data guardrail
│   └── commands/             # lesson slash commands
├── lessons/
│   ├── 0-getting-started/
│   ├── 1-foundations/
│   ├── 2-reusable/
│   ├── 3a-clinic/
│   ├── 3b-lab/
│   ├── 4-capstone/
│   └── graduation/
├── world/                    # fictional department, clinic, lab, cast, artifacts
├── data/                     # synthetic + openly licensed public datasets (with license notes)
├── workspace/                # where learners work; progress.md lives here
├── site/                     # GitHub Pages source (setup, reference guides, educators)
└── docs/
    ├── PLAN.md               # this file
    └── free-tier-budget.md   # request counts per lesson (§3.1)
```

## 8. For educators and professors

A dedicated section on the Pages site (`site/educators`) and in the README:

- **Where it fits:** practicum or clinical seminar (clinic path), research methods or stats lab (lab path), professional-development series, or first-year orientation (Modules 0–2 only).
- **Module-to-session map:** e.g., a 4-session version (M0–1 / M2 / path / capstone share-out) and a single-workshop version (M0–2 in a 3-hour block).
- **Adapting it (CC BY-SA):** how to fork the repo, swap in your own clinic or lab scenario and dataset, add lessons (e.g., neuropsych, assessment, supervision), and keep attribution and share-alike.
- **Assessment ideas:** the capstone as an assignment; a short reflection on what the learner would and wouldn't trust the agent with; peer review of each other's skills.
- **Before assigning:** check cost (Free-tier budget, institutional licenses or campus promotions), your institution's AI and data policies, and that students understand the no-real-data rule.
- **Facilitation tips:** pair nervous learners, budget time for setup, and know the common sticking points (from slice testing notes).

## 9. Build approach: vertical slices

Both paths ship in v1. There's no deadline: release when it's done. Build in vertical slices so the whole system works early.

**Slice 1, the walking skeleton:**
Download ZIP → bootstrap → Module 0 complete → one lesson each from Modules 1 and 2 (including open the hood) → the first lesson of **both** the clinic and lab paths → `progress.md` updating throughout → GitHub Pages site with setup instructions → first `free-tier-budget.md` entries.

Later slices fill in content within the proven structure.

## 10. Testing and success

**Per slice:**
- 1–2 real beginners (ideally trainees who've never used Cursor) go through the slice on **fresh Free accounts** while you **watch without helping** (a screen share is fine). Note every hesitation.
- You run it yourself on a **fresh Cursor install** to catch setup problems.
- Record free-tier request usage (§3.1).

**Success criterion for release:** a beginner gets from download to their first skill **without asking for help**, within the Free tier.

## 11. Licensing, contributions, upkeep

- **Content:** CC BY-SA 4.0. **Code** (rules, commands, scripts): MIT.
- **Contributions:** open via PRs, with you as final reviewer (likely post-v1). Doubles as a real first GitHub contribution for graduates.
- **Upkeep:**
  - Lessons avoid screenshots and exact menu paths where possible. The tutor describes the current UI.
  - Each module carries a "last tested with Cursor X.Y on [date]" stamp.
  - Rerun slices when Cursor ships major UI changes or changes its default model.

---

## Assumptions

| # | Assumption | Holds if… | Breaks if… | Resolve when |
|---|---|---|---|---|
| 1 | **Cursor's teaching tools work as planned.** Current names and layout for rules, slash commands and skills are unverified. | Slice 1 shows the tutor rule and lesson commands work as designed | Rules and commands can't carry multi-step lesson scripts | Slice 1 |
| 2 | **The agent follows lesson scripts** | The tutor stays on script and doesn't finish exercises for the learner | It skips checkpoints, or a default-model change shifts behavior | Every slice |
| 3 | **The Free tier (or $8 Plus) is enough.** Free limits are unpublished. | Modules 0–2 fit in Free with margin | Learners hit the limit before their first skill | Slice 1 budget test |
| 4 | **The data guardrail is a nudge.** The lesson is the real protection. | Learners take in "what never goes in" | Someone relies on the guardrail and pastes real data | Ongoing; watch in testing |
| 5 | **Suitable openly licensed psych datasets exist** | CC0/CC-BY data (e.g., OSF) that's realistic and messy | Good data requires DUAs or forbids redistribution | Before lab-path slice 2 |
| 6 | **A shared foundation works for both clinicians and researchers** | Neither group feels Modules 0–2 "aren't for me" | Testers from one group drop out before the split | Slice 1 testing (include one of each) |
| 7 | **Naming and trademark:** "Cursor" in the title may raise trademark issues (unconfirmed) | A neutral name, or confirmed acceptable | Forced rename after launch | Before public release |
| 8 | **Cursor's BAA status is unknown** and irrelevant while everything is synthetic | The go-live checklist tells learners to check BAA and institutional approval | The course implies real clinical use is fine | Capstone authoring |
| 9 | **Orca's site claims (e.g., star count) are unverified** | Only cited if verified | Repeated without checking | If Graduation references Orca |
| 10 | **Cost alternatives (BYO key on Free, etc.) are unverified** | One of them lowers the bar further | None work, and Plus is the floor | Slice 1 |
