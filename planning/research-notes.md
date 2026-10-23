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

**Unresolved:** a dataset with an explicit CC0/CC-BY license **and** demographic variables.
