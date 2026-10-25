**From:** Dr. Aisha Bello, Postdoc / Lab Manager, Foresight Lab
**To:** New Trainee
**Subject:** The dataset (and the rules)

Hi,

The dataset is in `data/` now: `EFT_Controls.csv`, plus `data-dictionary.md` and a README. It's a real, openly licensed dataset from an online study. Every row is an anonymous participant.

**Our question, decided before anyone looks at results:**

> Do people who did **episodic future thinking (EFT)** discount delayed rewards less than people in the two control conditions, **episodic recent thinking (ERT)** and **health information thinking (HIT)**?

The outcome is **`AUC`** (area under the discounting curve). The dictionary doesn't say which direction means "less discounting," so find out: have the agent explain AUC, then **check its explanation against the indifference-point columns** (`IP2`…`IP104`). Don't take its word for it, and don't guess.

**House rules for this analysis:**

1. **Read the data dictionary first.** All of it. Then check that it matches the actual columns. (Dictionaries drift. Ours certainly do.)
2. **Decide your exclusions before you compare the groups.** There's a column for manual exclusions and one for attention checks. Decide what you'll do with each, and **write down why**, before running the main test.
3. **One main test** for our question. Anything else you try is **exploratory**, and it gets labeled that way.
4. **Keep a log** of everything you tried, including the things that didn't work.
5. **Before you analyze: who's in this sample?** Summarize the demographics. We'll want to be honest about who these findings are about.

I'll be honest: an AI agent will happily run twenty tests until one of them is significant. The rules above are what stop that. They're the same rules that make preregistration work.

Aisha

*P.S. Henrik will ask for "a dashboard like that paper." Make the analysis right first. The dashboard is the easy part.*
