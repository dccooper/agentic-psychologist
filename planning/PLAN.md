# Repo Plan: The Agentic Psychologist

*Working title: "The Agentic Psychologist" (placeholder; see Assumption 7). Modeled on [Cursor for PMs](https://cursorforpms.com/): a course you learn **inside** the tool, not from a website.*

Status: plan, produced from a grilling session on 2026-10-21. Nothing built yet.

---

## 1. What this is

A free, open, downloadable course that teaches psychologists to use an AI coding agent (Google Antigravity IDE) by doing real work inside it. Learners go from "I've never opened an editor" to building their own reusable skills, an agent, and a small vibe-coded project, then take a first step toward common agentic-development practice (GitHub).

## 2. Audience and core problem

**Audience:** Psychology trainees, plus curious clinicians and researchers, who are new to AI tools.

**Core problem:** Fear and not knowing where to start, not missing features. The questions this course answers:
- What would I even use this for?
- Where do I start?
- The command line looks scary. Do I have to?

**Not a goal:** Getting AI tools adopted at an institution. This is an on-ramp, not an implementation program.

## 3. Tool

**Google Antigravity IDE for v1** (decided 2026-10-24; replaces Cursor). It has a graphical editor, a file Explorer and an agent panel, so learners don't start in a terminal. It's built on VS Code, and its layout is close to Cursor's original one. The Cursor for PMs format carries over unchanged.

**Why we left Cursor:** SpaceX/xAI acquired Cursor in 2026. Cursor's plans now come bundled with X subscriptions, and the $8 Plus plan is Grok-models-only. The Free plan was locked to Cursor Grok 4.6 Medium (QA pass 1). We don't want the course to promote Musk-owned products. David tested **VS Code + GitHub Copilot** and **Antigravity** side by side and chose Antigravity, because its layout is closer to classic Cursor.

**Portability (by design):** the tutor lives in `AGENTS.md` and the skills live in `.agents/skills/`. Antigravity, VS Code + Copilot, and Cursor all read both. Only `lessons/SCREEN_GUIDE.md` and the on-screen wording in lessons are tool-specific, so a future switch is cheap. **VS Code + Copilot Free (Microsoft) is the fallback** if Antigravity's free limits or speed fail.

**Antigravity specifics (verified from Google's docs, 2026-10-24):**
- **Rules:** `AGENTS.md` / `GEMINI.md` are read as always-on rules (24 KB per file; a 20k-token budget across always-on rules). The `.agents/rules/*.md` folder needs a `trigger:` frontmatter, or rules are silently dropped.
- **Skills:** `.agents/skills/<name>/SKILL.md` (`description` required). Docs confirm `/<skill>` invocation in the Antigravity *App*. Whether it works in the *IDE* is **unverified**, so `AGENTS.md` maps each `/command` to its skill file as a backstop.
- **Workflows** (`/name`) are being retired (they stop working 2026-10-19, migrate to skills). Don't use them.
- **Download trap:** the download page lists the **Antigravity App** (a separate desktop agent app) **first**. Learners need **Antigravity IDE (Standalone)**, further down. Setup instructions must steer them there.
- **Sign-in:** a Google account is required.
- **Default model:** Gemini 3.8 Flash (Medium by default; David also saw High). **A little slow. Monitor response time in every slice.**

- **Pi / Claude Code** (terminal agents) and **Orca** (running several agents in parallel, git-worktree based) were considered. Orca puts agents in terminal panes and assumes git plus an existing agent subscription, so it's a poor start for beginners. Both are candidates for **Graduation**, not v1.

### 3.1 Cost: keep the bar as low as possible

Antigravity pricing as checked on 2026-10-24: **Free** ($0, individuals): "a variety of agent models," unlimited Tab completions, **"basic weekly rate limits"** (no published numbers). Paid: **Google AI Pro** and **Google AI Ultra** (higher limits plus an AI credit pool; prices not shown on Antigravity's page, so check Google One). Business plans start at $30/seat/mo.

**Design for the default free model as the floor.** Lesson scripts can't depend on a stronger model's judgment. That's why scripts spell out expected answers, the tutor reads files rather than recalling them, and every slice is tested on a Free account. (On Cursor's free model in QA pass 1, the tutor invented a name at a checkpoint: QA-002.)

*(History: Cursor, checked 2026-10-21 and 2026-10-24, had Free locked to Grok 4.6 Medium; Plus $8, Grok-only; Premium $30 with third-party models extra. Dropped; see §3.)*

The tutor format uses requests heavily, since every exchange with the tutor is an agent request. So:

1. **Goal:** a learner on the Free plan can get from download to their first skill (end of Module 2) without paying. Ideally they can finish the whole course on Free.
2. **Lean lesson scripts:** checkpoints run in batches, the tutor doesn't chat for its own sake, and nothing is regenerated without a reason.
3. **Be honest about cost in Module 0:** "Free should get you through ___. If you hit the weekly limit, wait for it to reset or upgrade." No surprise paywalls. Weekly limits suit the pick-up/put-down design: a lesson a day, not a binge.
4. **Free-tier test protocol** (runs with every slice; see §10):
   - Testers use **brand-new Free accounts only**.
   - Record requests used per lesson (from Antigravity's usage/limits view if there is one, or the tester's notes), where the weekly limit was hit if it was, and what happened then. **Also record rough response times** (the default Gemini Flash felt slow).
   - Keep a running `planning/free-tier-budget.md`: requests per lesson, the cumulative total, and the point where Free runs out.
   - Exit criterion for v1: Modules 0–2 fit inside one week of Free limits with margin. If they don't, cut or batch lessons before considering a paid requirement.
5. **Alternatives to evaluate** (all unverified):
   - Google AI Pro as the paid fallback (check the price and whether students get it free or discounted).
   - Institutional Google Workspace accounts (some universities may block or allow Antigravity; covered in the educator section).
   - **VS Code + GitHub Copilot Free** (Copilot Pro $10/mo) as the backup tool. The course files already work there.

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
| **0. Getting started** | Shared | Install Antigravity IDE (the right download; Google sign-in), download the course, bootstrap, arrive at the department. *What never goes into an AI tool.* Honest note about cost. | 30 min |
| **1. Foundations** | Shared | Interface, files and folders, how much the agent may do on its own (review settings / planning vs. acting; to be mapped onto Antigravity's controls), @-context. First real tasks: meeting transcript → action items, rewrite an email to the director. | 1.5 h |
| **2. Making it reusable** | Shared | Rules files, templates, reusable pipelines, **first skill/command**. **Open-the-hood lesson** (§7.3). *The terminal isn't scary*: run one command on purpose. | 1 h |
| **3A. Clinic path** | Split | **Agent:** chief of staff for the clinic director (planning, project tracking, weekly review, personal-life planning too). **Vibe code:** a clinic marketing site or referral one-pager generator. | 2–3 h |
| **3B. Lab path** | Split | **Agent:** lab manager or literature-review assistant. **Vibe code:** an analysis script and small dashboard on a public dataset, in **Python** (R on request; rationale: most technical data-science roles use Python). | 2–3 h |
| **4. Capstone** | Shared | Build one thing for your own real, non-patient work, plus the go-live checklist. | Open-ended |
| **Graduation** | Optional | **GitHub for version control** (the editor's built-in Source Control or GitHub Desktop, not command-line git): a first taste of agentic-dev practice. Optional: publishing with GitHub Pages (only things built to be public; no API keys in code; Vercel mentioned as the next step), terminal agents (Pi / Claude Code), Orca. | Later |

Design rules:
- The paths split **after** Module 2. Everyone builds their first skill before choosing.
- **Both paths have the same shape:** one agent build plus one vibe-code project.
- Target about 5–6 hours to the capstone.
- **About 20 minutes per lesson, with marked pause points.** Every lesson ends with something that works.
- **Pick up, put down is taught, not just allowed:** agentic work resumes easily because it lives in files. Learners experience it (0.1 onward), understand it (2.2), and build it into their own agents (handoff notes in 3A.2b / 3B.2b).

## 7. How the course works

### 7.1 Distribution
- **One GitHub repo** holds the course files and the docs site.
- **The repo stays private until v1.** Then it goes public for comments. Until then, testers get a ZIP from David (no GitHub account needed).
- **GitHub Pages** hosts the site (Markdown + Jekyll, in `/docs`). Teaching happens in Antigravity, not on the site (except setup: the site's setup page walks through download and sign-in, since the tutor can't help before it's installed). The site has two parts:
  - **Front page: a showcase.** Sells the idea and gets people started right away (what it is, why it matters for psychologists, a demo, "Start in 5 minutes"). More polished than a standard docs theme. **Visual direction: David to bring reference examples.**
  - **Guide section, behind a menu:** detailed reference material, setup help, FAQs, the educator guide (§8), the concerns page (§8.5). A docs-style theme (e.g., Just the Docs).
- **Launch checklist (v1):** make repo public → turn on Pages → check that the site loads → check "Download ZIP" on a clean machine.
- Learners get the course with **"Download ZIP"** (no git required up front). An optional one-line bootstrap prompt ("Fetch [url] and help me start…") is offered as a convenience.

### 7.2 Teaching method
*Portable layout (2026-10-24):* the tutor is `AGENTS.md` and the skills are `.agents/skills/<name>/SKILL.md`. Antigravity, VS Code + Copilot, and Cursor all read these. See §3 for Antigravity specifics.

- **Tutor rule** (`AGENTS.md`, always on; it also maps each `/command` to its skill file, in case slash invocation doesn't fire in the IDE): the agent acts as a patient guide for psychologists. It moves one step at a time, explains why, **never does the learner's work for them**, and enforces the data guardrail.
- **A few navigation skills, not one skill per lesson:** `/start-course`, `/next-step`, `/im-stuck`, `/my-progress`. Each reads `workspace/progress.md` to find the current lesson, then reads that lesson's script in `lessons/`. Lesson scripts say what to teach, what the learner must do, and how to check it was done. Fewer skills means a cleaner `/` menu for beginners, and lessons stay plain markdown that's easy to edit.
- **Progress in files** (`workspace/progress.md`), updated by the agent, so learners can stop and resume.

### 7.3 Open the hood (decision B)
The course **works out of the box**. Learners don't build the machinery first. In Module 2 a lesson reveals: *"Everything that's been teaching you is made of the same things you're about to build."* The learner opens the tutor rule, opens the `/next-step` skill that's been driving every lesson, edits the tutor's tone and watches the change take effect, notices that `progress.md` has been the agent's memory all along, then builds their own first skill from that model.

### 7.4 Repo layout
```
/
├── README.md                 # what this is, quick start, links to Pages site
├── LICENSE-CONTENT           # CC BY-SA 4.0
├── LICENSE-CODE              # MIT
├── SETUP.md                  # install Antigravity IDE + Google sign-in + open the course
├── AGENTS.md                 # the tutor (always-on rule + data guardrail)
├── .agents/
│   └── skills/               # start-course, next-step, im-stuck, my-progress
├── lessons/                  # + SCREEN_GUIDE.md (on-screen directions, one place)
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
├── docs/                     # GitHub Pages site (Jekyll): landing page + guide
└── planning/
    ├── PLAN.md               # this file
    └── free-tier-budget.md   # request counts per lesson (§3.1)
```

## 8. For educators and professors

**Timing (decided):** a **lean guide ships in v1** (where it fits, module-to-session map, how to fork and adapt, checks before assigning, a "tell us you're using it" link). **A fuller guide is a fast follow in v2** (assessment rubrics, facilitation tips from testing notes, early-adopter stories).

A dedicated section in the site's guide (`docs/educators`) and in the README:

- **Where it fits:** practicum or clinical seminar (clinic path), research methods or stats lab (lab path), professional-development series, or first-year orientation (Modules 0–2 only).
- **Module-to-session map:** e.g., a 4-session version (M0–1 / M2 / path / capstone share-out) and a single-workshop version (M0–2 in a 3-hour block).
- **Adapting it (CC BY-SA):** how to fork the repo, swap in your own clinic or lab scenario and dataset, add lessons (e.g., neuropsych, assessment, supervision), and keep attribution and share-alike.
- **Assessment ideas:** the capstone as an assignment; a short reflection on what the learner would and wouldn't trust the agent with; peer review of each other's skills.
- **Before assigning:** check cost (Free-tier budget, institutional licenses or campus promotions), your institution's AI and data policies, and that students understand the no-real-data rule.
- **Facilitation tips:** pair nervous learners, budget time for setup, and know the common sticking points (from slice testing notes).

## 8.5 Site page: real concerns about AI

A page on the GitHub Pages site (and referenced from the README) that **takes concerns seriously and offers gentle, evidence-based pushback**. It's honest, not dismissive, and not evangelical.

**Two framings from David (keep these):**
1. **Environmental impact.** Data-center energy and water use is a real concern. But putting it in proportion helps: working through this course likely uses less water than binge-watching a season of a favorite show. **⚠️ This comparison must be sourced with current, citable figures before publishing (Assumption 11).** If the numbers don't support it, change the claim. Don't stretch it.
2. **Opting out is legitimate, but staying ignorant isn't safe.** Choosing not to use AI is a real and valid choice. But we can't afford to be ignorant of how these tools work, or we risk having them imposed on us (by employers, insurers, EHR vendors) without the knowledge to push back, set limits, or advocate for clients. **Understanding is what makes the choice yours.**

**Structure (decided):** the page leads with the **top four concerns**, with a **detailed FAQ nested underneath** for the rest. Each concern uses the same four parts: **the concern** (fairly stated, strongest form) → **what's true** → **gentle pushback** → **what this course does about it**.

- **Top four (proposed):** environment, opting out vs. ignorance, privacy (→ Lesson 0.2), accuracy / hallucination (→ 1.1 review-before-accept, 3B.2a citation trap).
- **FAQ:** bias (→ 3A.3b audience check, 3B.3a WEIRD-sample check), loss of skill (→ the tutor never does your work), jobs and the profession, cost and access (→ free-tier design, open license).
- **"Open questions" FAQ section:** *What we still don't know about AI, and where to read more.* Honest about unknowns, with pointers for further reading.

## 9. Build approach: vertical slices

Both paths ship in v1. There's no deadline: release when it's done. Build in vertical slices so the whole system works early.

**Slice 1, the walking skeleton:**
Download ZIP → bootstrap → Module 0 complete → one lesson each from Modules 1 and 2 (including open the hood) → the first lesson of **both** the clinic and lab paths → `progress.md` updating throughout → **site content drafted** in `/docs` (landing + setup page; it goes live at v1 because the repo is private until then) → first `free-tier-budget.md` entries.

Later slices fill in content within the proven structure.

## 10. Testing and success

**Per slice:**
- 1–2 real beginners (ideally trainees who've never used an AI editor) go through the slice on **fresh Free accounts** while you **watch without helping** (a screen share is fine). Note every hesitation.
- You run it yourself on a **fresh Antigravity IDE install**, starting from the download page, to catch setup problems.
- Record free-tier request usage (§3.1).
- Record the **Antigravity version, model, and review setting** chosen during setup, plus **rough response times**. The tutor's accuracy and pace depend on the model.
- Log findings in `QA/<pass name>/` (error log + screenshots). After fixes, re-run the **UI claims** in each lesson's "UI this lesson depends on" list against `lessons/SCREEN_GUIDE.md`.

**Success criterion for release:** a beginner gets from download to their first skill **without asking for help**, within the Free tier.

## 11. Licensing, contributions, upkeep

- **Content:** CC BY-SA 4.0. **Code** (rules, commands, scripts): MIT.
- **Contributions:** open via PRs, with you as final reviewer (likely post-v1). Doubles as a real first GitHub contribution for graduates.
- **Upkeep:**
  - Lessons avoid screenshots and exact menu paths where possible. On-screen directions live in one file, `lessons/SCREEN_GUIDE.md` (labels first; ✅ verified / ⚠️ inferred), which lessons point to. When the editor changes, update that file.
  - Each module carries a "last tested with Antigravity X.Y on [date]" stamp.
  - Rerun slices when Antigravity ships major UI changes or changes its default model.

---

## Assumptions

| # | Assumption | Holds if… | Breaks if… | Resolve when |
|---|---|---|---|---|
| 1 | **Antigravity's teaching tools work as planned.** `AGENTS.md` and `.agents/skills/` are documented. In Cursor (QA pass 1), skills drove multi-turn lessons and updated `progress.md`. Unverified in Antigravity: whether `/start-course` triggers the skill in the IDE, or only the `AGENTS.md` backstop does. | Slice 1 retest shows the commands drive lessons | Neither the slash command nor the backstop works reliably | QA pass 2 |
| 2 | **The agent follows lesson scripts on the default free model** (Gemini 3.8 Flash) | The tutor stays on script, reads files rather than guessing, and doesn't finish exercises for the learner | It skips checkpoints or invents facts (seen on Cursor's Grok: QA-002), or it's too slow for a 20-minute lesson | Every slice, always on a Free account |
| 3 | **Antigravity's Free weekly limits are enough.** Limits are unpublished. | Modules 0–2 fit in a week of Free with margin | Learners hit the weekly limit before their first skill | Slice 1 budget test |
| 4 | **The data guardrail is a nudge.** The lesson is the real protection. | Learners take in "what never goes in" | Someone relies on the guardrail and pastes real data | Ongoing; watch in testing |
| 5 | **Suitable openly licensed psych datasets exist.** *Largely resolved 2026-10-23:* OSF bfxnv (CC BY 4.0, demographics, paired PLOS paper). See `research-notes.md`. Remaining: data dictionary review. | CC0/CC-BY data (e.g., OSF) that's realistic and messy | Good data requires DUAs or forbids redistribution | Before lab-path slice 2 |
| 6 | **A shared foundation works for both clinicians and researchers** | Neither group feels Modules 0–2 "aren't for me" | Testers from one group drop out before the split | Slice 1 testing (include one of each) |
| 7 | **Naming and trademark:** keep tool names (Google, Antigravity, Cursor) out of the course title | A neutral name ("The Agentic Psychologist") | Forced rename after launch | Before public release |
| 8 | **Antigravity's BAA status (Free, personal Google account) is unknown** and irrelevant while everything is synthetic. Setup's data-use checkbox defaults to *on* (Google may use interactions) | The go-live checklist tells learners to check BAA and institutional approval | The course implies real clinical use is fine | Capstone authoring |
| 9 | **Orca's site claims (e.g., star count) are unverified** | Only cited if verified | Repeated without checking | If Graduation references Orca |
| 10 | **Cost fallbacks (Google AI Pro, student offers, VS Code + Copilot Free) are unverified** | One of them works if Free runs out | None fit the course | Slice 1 |
| 12 | **Antigravity stays free and stable.** It's a young product (Workflows were retired within months) | Free tier and the IDE persist | Google retires the standalone IDE or the Free tier | Check every slice; the portable layout limits the damage |
| 11 | **"The course uses less water than binge-watching a season" is unsourced** | Current per-query AI water/energy estimates and streaming estimates, from citable sources, support it | The figures don't support it, or estimates vary too widely to say | Before the concerns page is published |
