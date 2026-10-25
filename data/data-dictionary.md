# Data Dictionary for EFT-Controls

*Converted from the authors' `Data Dictionary for EFT Controls.docx` to Markdown for this course. The wording below is the authors', unchanged except for formatting (headings and bullet lists added). Licensed CC BY 4.0; see `data/README.md`.*

## `Manual.Excl`

This column contains the reason for excluding this participant's data from analysis, if applicable. If their data passed criteria, then no reason is listed.

## `AC.PassBoth`

Whether participants responded correctly on the two attention check questions embedded in the discounting assessment. There were no participants who passed the quality check for their cues who did not pass at least one attention check. The only participants who missed both (which was still rare) were rejected, so any "No" means they passed at least one check.

## `Q.ID`

Qualtrics-generated random survey code

## `Age`

Age in years, entered into a textbox that only accepts numeric characters. No other limits

## `Sex`

From drop-down box. Possible response options of "Male", "Female", "Other", and "Prefer not to respond".

## `HispLatinx`

Indicates whether participant identified as Hispanic/Latinx, or preferred not to respond. Possible options of "Hisp/Latinx", "NotH/L", and "N/A". This was inferred from a question that listed Hispanic/Latino in a single question with races (see below)

## `Race.Eth.Comb`

Values are (and represent):

- 1 = American Indian or Alaska Native
- 2 = Asian
- 3 = Black or African American
- 4 = Hispanic or Latino
- 5 = Native Hawaiian or Pacific Islander
- 6 = White
- 7 = Multiple
- 8 = Prefer not to respond
## `Income`

Yearly personal income in USD (not household, before taxes), entered into a textbox that only accepts numeric characters. No other limits. Blank indicates participant preferred not to respond.

## `SubSES.US`

MacArthur Ladder for subjective SES, U.S.-based ranking. 10 is highest among those in the U.S generally, and 1 is lowest among those in the U.S. generally. Blank is preferred not to respond.

## `SubSES.Comm`

Same as above, but for the individual relative to those in their community.

## `Edu.Years`

Years of education completed, obtained from a drop-down box of fixed numbers of years. Blank is preferred not to respond (but no one actually indicated they preferred not to).

## `Edu.Lvl`

Highest level of education completed, obtained from a multiple choice question. Participants had the ability to say "Prefer not to respond' and "Other". No one endorsed "Other". Blank is preferred not to respond. These data are not reported in the paper because level obtained did not differ across groups and was largely redundant with years completed.

- 0.5 = Prefer not to respond
- 0 = None (no high school diploma or equivalent)
- 1 = High school diploma or equivalent
- 2 = Associate's degree
- 3 = Bachelor's degree
- 4 = Master's degree
- 5 = Doctorate
- 6 = Professional (MD, JD, DDS)
## `Multitask`

Participants were asked if they engaged in other activities while working on the HIT. Response options were 5 non-target HIT activities of various types (e.g., employer-provided work, leisurely activities), no other activities, other, and prefer not to respond. There was very little variability so responses were recoded into "Yes", "No", and "N/A" depending on what they endorsed.

## `Survey.Duration`

Duration in minutes from the time the participant opened the survey until they got to the final survey page. Decimals reflect fractions of minutes.

## `Group`

The group that participants were randomly assigned to for the thinking/thought task activities.

- EFT = Episodic Future Thinking
- ERT = Episodic Recent Thinking
- HIT = Health Information Thinking
## `AUC`

Area under the curve (AUC) formed by participants' indifference points.

## `JB1`

This column indicates the number of times an individual's indifference points met the nonsystematic criteria ("jumps up" from one indifference point to the next). Did not use in analyses since it's atypical with EFT

## `JB2`

This column indicates whether or not an individual's indifference points met the criteria for non-discounting. Did not use in analyses since it's atypical with EFT

## `Avg.Vivid.Elab`

Participants were asked, after each block of discounting questions, how vividly they could imagine the identified events. This number is the average score provided across all events, with the individual ratings coming from a scale of 1 (not at all) to 5 (very much). This is only relevant to EFT and ERT participants.

## `Avg.Vivid.Check`

Participants were asked, after each block of discounting questions, how vivid their thoughts were about their displayed cues/events. This number is the median score provided across all blocks, with the individual ratings coming from a scale of 1 (not at all) to 5 (very much).

## `Avg.Freq.Check`

Participants were asked, after each block of discounting questions, how frequently they thought about their displayed cues/events. This number is the median score provided across all blocks, with the individual ratings coming from a scale of 1 (not at all) to 5 (very much).

## `Prev.DD`

Participants were asked whether they had previously completed something akin to a DD task

## `Prior.EFT`

Participants were asked whether they had previously completed something akin to EFT/ERT procedures.

## `Pos.Affect`

Scores from the PANAS for the positive items (individual scores 1-5, from very slightly/not at all to extremely), expressed as the average rating. Some individuals did not respond to all questions, which precluded using the sum.

## `Neg.Affect`

Scores from the PANAS for the negative items (individual scores 1-5, from very slightly/not at all to extremely), expressed as the average rating. Some individuals did not respond to all questions, which precluded using the sum.

## `NAs.PA`

Number of positive items from the PANAS the participant did not include a response for

## `NAs.NA`

Number of negative items from the PANAS the participant did not include a response for

## `IP2-IP104`

Indifference points from the delay discounting assessment, with the terminal number referring to the delay (expressed in weeks)

## `BMI`

Body mass index, calculated from participants' self-reported height and weight. Blank indicates the participant preferred not to respond to one or more questions needed to calculate.

## `Ht.In`

Participants' height in inches. Blank indicates participants preferred not to respond.

## `Wt.In`

Participants' weight in inches. Blank indicates participants preferred not to respond.

## `ET.Duration`

Duration of time spent on EFT/ERT/HIT activities. This is calculated from time stamps for the moment the instructions were first displayed, and the moment the participant finished that survey block.

## `DD.Duration`

Duration of time spent completing the DD task. This is calculated from time stamps for the moment the DD instructions were displayed, and the moment the participant finished the DD portion of the survey.
