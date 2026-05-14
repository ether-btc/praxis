---
name: praxis-decision-analysis
description: >
  MANDATORY trade-off evaluation. Invoke when facing a choice between alternatives —
  build-vs-buy, rewrite-vs-patch, technology selection, resource allocation, priority
  decisions. Do NOT default to the first reasonable option. Do NOT skip evaluating
  "do nothing" as a valid alternative. Run weighted criteria analysis with second-order
  consequences before recommending.
version: 1.0.0
author: ether-btc (ported from xD4O/praxis)
license: MIT
metadata:
  hermes:
    tags: [reasoning, decision-analysis, trade-offs, mandatory]
    related_skills: [praxis-problem-classification, praxis-strategic-reasoning]
---

# Decision Analysis Protocol

> **MANDATORY — Do not default to the first reasonable option.**

## STEP 1 — Frame the real decision

State the decision in one sentence. Then check:
- Are these actually the only options? What's the third option nobody mentioned?
- Is this the right decision to be making?
- Is this reversible (Type 2) or irreversible (Type 1)?

Type 2 → Spend 10 minutes. Decide and iterate.
Type 1 → Spend proportional effort. Get it right.

## STEP 2 — Enumerate options

List ALL viable options, including:
- The options the user named
- "Do nothing" (always a valid option — what happens if we don't decide?)
- The hybrid/phased approach (80% of the benefit now?)

For each option, state in one sentence what it optimizes for.

## STEP 3 — Define criteria and weight them

List 4-6 criteria that matter. Assign weights (1-5).

Common: cost, speed to deliver, risk, maintainability, team capability,
scalability, user impact, reversibility.

Ask the user which criteria matter most. Do NOT assume.

## STEP 4 — Score and calculate

For each option, score each criterion (1-10). Multiply by weight. Sum.

| Option | Criterion A (×W) | Criterion B (×W) | ... | Total |
|---|---|---|---|---|

If two options are within 10% of each other, proceed to Step 5 for tiebreaking.

## STEP 5 — Second-order analysis

For the top 1-2 options, apply:

**Second-order thinking:** What happens 6 months after we choose this?

**Pre-mortem:** Assume we chose this option and it failed badly in 6 months.
What went wrong? Is that failure preventable?

**Steelman the loser:** Make the best possible case for the option you're
NOT recommending. If the steelmanned case is compelling, reconsider.

## STEP 6 — Recommend with confidence

```
RECOMMENDATION: [Option X]
├── Why: [1-2 sentence justification tied to highest-weighted criteria]
├── Key risk: [the most likely way this goes wrong]
├── Mitigation: [how to address that risk]
├── Reversibility: [Type 1/2, what undo looks like]
└── Confidence: [HIGH / MEDIUM / LOW]
```

If confidence is LOW, state what additional information would increase it.

## HARD-GATE

Do NOT recommend an option without:
- At least 3 options evaluated (including "do nothing")
- Explicit criteria with weights confirmed by the user
- Second-order consequences considered
- Confidence level stated

## Handoff

After recommendation is made and user accepts:

Proceed to `development/plan` for implementation planning. Pass the chosen option,
criteria weights, and key risks as context.

## Rationalization catching

STOP if you catch yourself thinking:
- "Let's just go with X" — Evaluate at least 3 options including "do nothing."
- "The first option looks fine" — Anchoring bias. The first option is rarely the best.
- "We don't need 'do nothing'" — Do nothing is always a valid option. State why it's not.
- "I know what's right" — The skill ensures you evaluated alternatives, not just asserted.