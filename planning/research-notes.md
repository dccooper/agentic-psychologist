# Research Notes

Findings for open research items. Searched 2026-10-23.

## Assumption 11: Water comparison ("less than binge-watching a season")

**Verdict: plausible under most published estimates, but not under the most pessimistic ones. Phrase it carefully and cite it.**

| Source | Estimate |
|---|---|
| Google (Gemini, median text prompt) | ~0.26 mL onsite; ~1 mL including power-generation water ([arXiv 2508.15734](https://arxiv.org/pdf/2508.15734)) |
| OpenAI (reported) | ~0.32 mL per prompt |
| Mistral (Le Chat lifecycle assessment) | ~45 mL per ~400-token response |
| Older academic (GPT-3) | ~7–48 mL per medium response, location-dependent ([arXiv 2505.09598](https://arxiv.org/pdf/2505.09598) and related work) |
| Streaming video | ~2–12 L per hour (MIT-linked estimate; [MIT Climate](https://climate.mit.edu/posts/how-reduce-environmental-impact-your-next-virtual-meeting)) |

**Rough math:**
- A season binge (~8–10 h) ≈ **16–120 L**.
- Course: N agent requests (unknown; free-tier testing will measure this). **Caveat: agentic requests are heavier than a "median text prompt"** because they carry large context and use tools. Assume about 10× a chat prompt.
- At ~10 mL/request × ~300 requests ≈ **3 L** → comfortably less than a season.
- At Mistral's 45 mL × 10× agentic × 300 ≈ **135 L** → could exceed a season.

**Suggested wording:** *"Based on published estimates from Google and OpenAI, working through this whole course likely uses less water than streaming one season of a TV show. Estimates vary widely and AI companies disclose little, so see our sources."*

**Action:** after free-tier testing gives a real request count, rerun the math. Anthropic has published no per-query figures (as of this search).

## Assumption 5 + lit-review papers: dataset and papers

**Idea:** PLOS ONE publishes under CC BY 4.0 by default and requires data sharing. **One paper plus its own open dataset** = a coherent lab path: read it in 3B.2, analyze its data in 3B.3.

**PLOS ONE candidates (future thinking; CC BY by journal policy):**
- 10.1371/journal.pone.0270661: Noreen & Dritschel (2022), *In the here and now: Future thinking and social problem-solving in depression*
- 10.1371/journal.pone.0289676: (2023) *Thinking about the consequences: the detrimental role of future thinking on intrapersonal problem-solving in d…*
- 10.1371/journal.pone.0188079: (2017) *Episodic future thinking reduces temporal discounting in healthy adolescents*
- 10.1371/journal.pone.0217224: (2019) *Concreteness and emotional valence of EFT independently affect…*
- 10.1371/journal.pone.0214397: (2019) *Improvements in EFT methodology: a standardized episodic thinking control*
- 10.1371/journal.pone.0237435: (2020) *Translating EFT manipulations for clinical use*

**Dataset candidate checked:** Noreen & Dritschel, OSF [osf.io/sdnh7](https://doi.org/10.17605/osf.io/sdnh7). Public, one SPSS file (`.sav`, 18 KB). **⚠️ No license set on the OSF project**, so redistributing it in the repo isn't clearly permitted. The lesson could have learners download it from OSF themselves, or we could ask the authors to add a CC-BY license.

**Not yet checked:** data availability and licenses for the other PLOS candidates; OSF cybfu (Morales Valiente et al., 2024); the OSF directory of open psychology datasets.

### Other candidates checked (2026-10-23)

| Paper | Data location | License | Notes |
|---|---|---|---|
| **pone.0237435** (2020) *Translating EFT manipulations for clinical use* | **OSF [bfxnv](https://doi.org/10.17605/OSF.IO/BFXNV)** | **CC BY 4.0 ✅** | **← Recommended.** See below. |
| pone.0217224 (2019) | figshare 7072568 | CC BY 4.0 | Raw `.mt` mouse-tracking files; too complex for beginners |
| pone.0188079 (2017) | PLOS supporting information (S1–S3 .txt) | CC BY (PLOS SI) | Backup option; not inspected |
| pone.0214397 (2019) | OSF 6nsqb | None set | `.xls` |
| pone.0289676 (2023) | OSF j3bxs | None set | Small `.sav` |
| pone.0289478 (2023) | GitHub repo | None set | R project |
| pone.0270661 (2022) | OSF sdnh7 | None set | Small `.sav` (OSF fallback) |

### ✅ Recommended: OSF bfxnv + PLOS ONE 0237435

*"Development of a Clinical EFT Control: Data Set."* CC BY 4.0. Files: `EFT_Controls.csv` (254 rows × 39 cols), a data dictionary (.docx), and the authors' R Markdown analysis scripts.

**Why it fits the lab path almost perfectly:**
- **Fits the Foresight Lab:** episodic future thinking and delay discounting.
- **Three groups:** EFT (77), ERT (90), HIT (87). A clear pre-stated question for Dr. Bello: *does EFT reduce delay discounting (`AUC`) compared with the control conditions?*
- **Demographics for the bias check:** Age (22–81, mean 36), Sex, Race/ethnicity, Hispanic/Latinx, Income, subjective SES, Education. A quick look shows the race/ethnicity code `6` = 191 of 254 (likely White, to confirm in the data dictionary) and 17/254 Hispanic/Latinx, so the WEIRD-sample check has something real to find.
- **Realistic mess:** numerically coded race and education (you need the data dictionary), manual exclusions (`Fail.Writing` 52, `Outside.US` 4), attention-check failures (38). A natural teaching moment about **exclusion decisions as forking paths**.
- **Reproducibility hook:** the authors' own R scripts are included. Python learners can check whether their result matches the published one, and R learners can run the original.

**To do:** read the data dictionary (codes for race, education, groups); confirm the paper's main result; add **only the CSV and data dictionary** to `data/` with an attribution file (CC BY requires credit). **Don't add the authors' R scripts or the paper.** They're held back for the blind-comparison reveal in 3B.3b (see OUTLINE firewall note).
