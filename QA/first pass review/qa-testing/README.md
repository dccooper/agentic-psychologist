# Course QA — Vertical Slice 1

**Handoff for coding agent** | Captured October 23–24, 2026

## Start here

1. Read [`agent-fix-plan.md`](agent-fix-plan.md) for proposed fixes and acceptance criteria.
2. Read [`error-log.md`](error-log.md) for exact observations, quotes, and evidence.
3. Use [`tests/ui-instruction-matrix.md`](tests/ui-instruction-matrix.md) to reproduce UI-related failures; [`tests/README.md`](tests/README.md) describes the proposed regression approach.
4. Review [`screenshots/`](screenshots/) for source evidence. Screenshot filenames are referenced via relative paths in the Markdown files.

## Scope

- **5 open bugs**: QA-001 through QA-005.
- **4 instructional improvements**: NOTE-001 through NOTE-004.
- **8 screenshots**, covering UI layout, filename navigation, incorrect name, mode picker, compliance exercise, Markdown intro, and review workflow.
- All findings are **reported/unresolved**; proposed fixes and proposed tests have **not** been implemented or run.

## Agent implementation guidance

- Locate the source lesson scripts, prompts, fixtures, and course artifacts in the target repository; this QA package does not include that repository.
- Address the shared Cursor UI language problems (QA-001, QA-003, QA-004, QA-005) consistently, rather than only changing isolated sentences.
- Preserve lesson sequence and existing checkpoints; do not reveal compliance quiz answers before the learner responds.
- For QA-002, ground the sender name in the actual welcome email (`Dr. Miriam Okafor`).
- Implement improvements separately from defect fixes where possible. Add clear post-activity learning takeaways.
- Verify the supported Cursor build and click-through UI before hard-coding mode or accept/reject control names. Screenshots are point-in-time evidence, not a complete UI specification.
- Record the actual files edited and test outcomes in the coding agent's completion report.

## File structure

```text
qa-testing/
├── README.md
├── error-log.md
├── agent-fix-plan.md
├── screenshots/
│   ├── issue-001-before.png
│   ├── issue-001-after.png
│   ├── issue-002-name-mismatch.png
│   ├── issue-003-mode-picker.png
│   ├── issue-004-cursor-layout.png
│   ├── issue-005-review-changes.png
│   ├── note-002-compliance-exercise.png
│   └── note-004-markdown-intro.png
└── tests/
    ├── README.md
    └── ui-instruction-matrix.md
```
