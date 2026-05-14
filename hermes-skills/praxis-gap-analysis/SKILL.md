---
name: praxis-gap-analysis
description: >
  MANDATORY validation. Invoke before presenting any design, plan, architecture decision,
  or significant recommendation as final. Runs 7 cognitive debiasing checks: inversion,
  second-order effects, MECE coverage, map vs territory, adversarial, simplicity, and
  reversibility. Do NOT present conclusions without running all 7 checks.
version: 1.0.0
author: ether-btc (ported from xD4O/praxis)
license: MIT
metadata:
  hermes:
    tags: [reasoning, gap-analysis, validation, mandatory]
    related_skills: [praxis-problem-classification, praxis-architecture-reasoning]
---

# Gap Analysis Protocol

> **MANDATORY — Before presenting a design or plan as final, run all 7 checks.**

## CHECK 1 — Inversion

Ask: "How would I guarantee this fails?"

List 3 specific failure modes. For each, verify your solution prevents it.
If any failure mode is not prevented, flag it as an open risk.

## CHECK 2 — Second-order consequences

Ask: "And then what?" three times.

- 1st order: [immediate intended effect]
- 2nd order: [effect of that effect — often unintended]
- 3rd order: [cascading consequence — often counterintuitive]

If 2nd or 3rd order effects are negative, state whether they're acceptable or
require design changes.

## CHECK 3 — MECE coverage

Ask: "Have I covered the entire problem space with no gaps and no overlaps?"

List the dimensions you've addressed. Identify any dimension you haven't
addressed. Gaps are where surprises live.

## CHECK 4 — Map vs territory

Ask: "Where does my model diverge from reality?"

List 3 things you simplified, assumed, or ignored. For each, state the risk
if reality differs from your model.

## CHECK 5 — Adversarial

Ask: "How would a hostile actor exploit this? How would a careless user break this?"

Identify the weakest point. State whether it's acceptable or needs hardening.

## CHECK 6 — Simplicity

Ask: "Is there a simpler solution I'm overlooking?"

If yes, state why you chose the more complex approach. The justification must
be concrete, not "it might be needed later" (YAGNI violation).

## CHECK 7 — Reversibility

Ask: "Is this decision reversible?"

- If YES (Type 2): Proceed. Note that it can be unwound if wrong.
- If NO (Type 1): Have you applied proportional rigor? Would you bet your
  job on this recommendation?

## Output format

```
GAP ANALYSIS COMPLETE
├── Inversion: [X/3 failure modes mitigated] [open risks if any]
├── Second-order: [acceptable / requires changes]
├── MECE: [complete / gap in: ___]
├── Map vs territory: [top risk: ___]
├── Adversarial: [weakest point: ___]
├── Simplicity: [simplest viable / justified complexity]
├── Reversibility: [Type 1 / Type 2]
└── Confidence: [HIGH / MEDIUM / LOW / INSUFFICIENT]
```

## HARD-GATE

Do NOT present a design, plan, or recommendation as final until all 7 checks
are complete. If any check reveals a critical issue (unmitigated failure mode,
negative 2nd-order effect, MECE gap, or Type 1 decision with LOW confidence),
you MUST address it before proceeding.

## Handoff

After all 7 checks pass and the design is validated:

Proceed to `development/plan` for implementation planning. Pass the validated
design and any issues flagged during gap analysis.

## Rationalization catching

STOP if you catch yourself thinking:
- "This is straightforward" — straightforward things don't need gap analysis.
- "The user is in a hurry" — a 2-minute check saves a 2-week failure.
- "I already considered this" — show your work. Implicit checks don't count.
- "The design looks good" — Gap analysis catches what design intuition misses.