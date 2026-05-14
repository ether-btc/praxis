---
name: praxis-strategic-reasoning
description: >
  MANDATORY strategic analysis. Invoke for business decisions, product strategy,
  competitive analysis, roadmap prioritization, or any decision about WHAT to build
  rather than HOW to build it. Do NOT present strategy without measurable OKRs.
version: 1.0.0
author: ether-btc (ported from xD4O/praxis)
license: MIT
metadata:
  hermes:
    tags: [reasoning, strategic, business-analysis, mandatory]
    related_skills: [praxis-problem-classification, praxis-decision-analysis]
---

# Strategic Reasoning Protocol

> **MANDATORY — This isn't a code problem — it's a strategy problem. Different tools.**

## STEP 1 — Clarify the real job

Ask: "What job is the user actually hiring this solution for?"

The stated goal is often not the real goal:
- "We need a dashboard" → Real job: "Convince the board we're growing"
- "Add feature X" → Real job: "Stop losing customers to competitor Y"
- "Rewrite in Rust" → Real job: "Our system can't handle next year's scale"

State the real job in one sentence. Confirm with the user.

## STEP 2 — Situational assessment (SWOT)

Complete all four quadrants. Each must have 3+ items.

- **Strengths** (internal, positive): What advantages exist today?
- **Weaknesses** (internal, negative): What limitations constrain you?
- **Opportunities** (external, positive): What trends or gaps can you exploit?
- **Threats** (external, negative): What could undermine you?

Then cross-reference:
- How can strengths capture opportunities?
- How do weaknesses amplify threats?
- Which Strength+Opportunity pair is the highest-leverage play?

## STEP 3 — Competitive landscape

If competitors or alternatives are relevant, map them:
- Who else solves this job? (direct competitors, substitutes, "do nothing")
- What do they do better? What do they do worse?
- Where is the uncontested space they don't occupy?

State the differentiation strategy in one sentence.

## STEP 4 — Prioritize ruthlessly

**Impact vs effort matrix:** For each initiative, estimate impact (1-10) and
effort (1-10). High impact + low effort = do first.

**Constraint check:** What's the bottleneck? Time, money, people, skill?
Which initiatives are blocked by the same constraint? Resolve the constraint
first, or accept that blocked initiatives won't happen.

**Kill candidates:** Which initiatives should be explicitly STOPPED?
Name them. Stopping things requires the same rigor as starting things.

## STEP 5 — Define success measurably

For the recommended strategy, define OKRs:

**Objective:** Qualitative, inspiring, one sentence.
**Key Results:** 2-3 quantitative measures, each:
- Specific (exact metric, exact target)
- Measurable (can verify with a dashboard or report)
- Time-bound (by when)

Test: "Can someone other than me verify whether this KR is met?" If no, it's
not measurable enough.

## Output format

```
STRATEGIC ANALYSIS
├── Real job: [one sentence]
├── Top strength × opportunity: [the highest-leverage play]
├── Differentiation: [one sentence]
├── Top priority: [what to do first and why]
├── Kill list: [what to stop doing]
├── OKR: [objective + 2-3 key results]
└── Confidence: [HIGH / MEDIUM / LOW]
```

## HARD-GATE

Do NOT present a strategic recommendation without:
- The real job stated and confirmed with the user
- All 4 SWOT quadrants completed with 3+ items each
- At least one initiative explicitly on the kill list
- OKRs with measurable, verifiable key results

## Handoff

After the strategic analysis is complete and the user confirms the direction:

Proceed to `development/plan` to translate the strategic direction into an
implementation plan. Pass your real job statement, SWOT cross-references,
kill list, and OKRs as context.

## Rationalization catching

STOP if you catch yourself thinking:
- "The user already knows their strategy" — Then validate it. SWOT takes 2 minutes.
- "This is just a quick feature decision" — If it affects what to build vs how, it's strategy.
- "We don't need OKRs for this" — If you can't measure success, you can't verify it.
- "The market already moved" — Strategy still needs to be reasoned, even in fast-moving markets.
- "We've always done it this way" — That's a weakness, not a strength.