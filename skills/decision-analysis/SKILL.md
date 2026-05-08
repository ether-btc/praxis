---
name: decision-analysis
description: >
  MANDATORY trade-off evaluation. You MUST invoke this skill when the user faces a choice
  between alternatives — build-vs-buy, rewrite-vs-patch, technology selection, resource
  allocation, priority decisions. Do NOT default to the first reasonable option. Do NOT
  skip evaluating "do nothing" as a valid alternative. Invoke this to run weighted criteria
  analysis with second-order consequences before recommending.
---

# Decision Analysis Protocol

EXTREMELY_IMPORTANT: This is a MANDATORY protocol, not a suggestion. Follow every step.
Do not skip steps. Do not combine steps. Do not summarize. Work through each gate in order.

You're choosing between alternatives. Do NOT default to the first reasonable option.
Work through this protocol to find the best option — or discover the question is wrong.

## STEP 1 — Frame the real decision

State the decision in one sentence. Then check:

- Are these actually the only options? What's the third option nobody mentioned?
- Is this the right decision to be making? (Sometimes the meta-question matters more)
- Is this reversible (Type 2) or irreversible (Type 1)?

Type 2 → Spend 10 minutes on this protocol. Decide and iterate.
Type 1 → Spend proportional effort. Get it right.

## STEP 2 — Enumerate options

List ALL viable options, including:
- The options the user named
- "Do nothing" (always a valid option — what happens if we don't decide?)
- The hybrid/phased approach (is there a way to get 80% of the benefit now?)

For each option, state in one sentence what it optimizes for.

## STEP 3 — Define criteria and weight them

List 4-6 criteria that matter for this decision. Assign weights (1-5).

Common criteria: cost, speed to deliver, risk, maintainability, team capability,
scalability, user impact, reversibility.

Ask the user which criteria matter most. Do NOT assume.

## STEP 4 — Score and calculate

For each option, score each criterion (1-10). Multiply by weight. Sum.

Present as a table:

| Option | Criterion A (×W) | Criterion B (×W) | ... | Total |
|---|---|---|---|---|

If two options are within 10% of each other, the decision matrix alone is
insufficient. Proceed to Step 5 for tiebreaking.

## STEP 5 — Second-order analysis

For the top 1-2 options, apply:

**Second-order thinking:** What happens 6 months after we choose this?
What's the 2nd-order consequence? The 3rd-order?

**Pre-mortem:** Assume we chose this option and it failed badly in 6 months.
What went wrong? Is that failure preventable?

**Steelman the loser:** Make the best possible case for the option you're
NOT recommending. If the steelmanned case is compelling, reconsider.

## STEP 6 — Recommend with confidence

State your recommendation explicitly:

```
RECOMMENDATION: [Option X]
├── Why: [1-2 sentence justification tied to highest-weighted criteria]
├── Key risk: [the most likely way this goes wrong]
├── Mitigation: [how to address that risk]
├── Reversibility: [Type 1/2, what undo looks like]
└── Confidence: [HIGH / MEDIUM / LOW]
```

If confidence is LOW, state what additional information would increase it,
and recommend gathering that information before committing.

<HARD-GATE>
Do NOT recommend an option without:
- At least 3 options evaluated (including "do nothing")
- Explicit criteria with weights confirmed by the user
- Second-order consequences considered for the recommendation
- Confidence level stated

This skill prevents:
- "Let's just go with X" without evaluating alternatives
- Anchoring on the first option considered
- Ignoring "do nothing" as a valid choice
- Making irreversible decisions with reversible-decision rigor
</HARD-GATE>

## Superpowers handoff

After recommendation is made and user accepts:

If Superpowers is installed and the decision leads to building something → invoke
`Skill(superpowers:brainstorming)` with the chosen option, criteria weights, and key
risks as context. Let Superpowers drive the design of the chosen approach.

If Superpowers is NOT installed → proceed to design or implementation based on the
recommendation.

<RATIONALIZATION-CATCHING>
If you find yourself thinking any of these, you are about to violate the protocol:

- "Let's just go with X" — Evaluate at least 3 options including "do nothing."
- "The first option looks fine" — Anchoring bias. The first option is rarely the best.
- "We don't need 'do nothing'" — Do nothing is always a valid option. State why it's not.
- "I know what's right" — The skill ensures you evaluated alternatives, not just asserted.
- "This is a quick decision" — Quick decisions with long tails need the same rigor.
- "The user asked for X" — The skill ensures you evaluated alternatives, not just obeyed.
</RATIONALIZATION-CATCHING>
