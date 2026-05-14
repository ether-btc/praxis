---
name: praxis-architecture-reasoning
description: >
  MANDATORY architecture analysis. Invoke before module boundary decisions, build-vs-buy
  choices, technology selections, data model designs, API contracts, or any structural
  decision that is expensive to reverse. Do NOT propose architecture without running
  reversibility classification, boundary analysis, and bottleneck identification.
version: 1.0.0
author: ether-btc (ported from xD4O/praxis)
license: MIT
metadata:
  hermes:
    tags: [reasoning, architecture, analysis, mandatory]
    related_skills: [praxis-problem-classification, praxis-gap-analysis]
---

# Architecture Reasoning Protocol

> **MANDATORY — These decisions are expensive to reverse. Reason carefully.**

## STEP 1 — Classify the decision's reversibility

**Type 1 (one-way door):** Database schema, public API contract, core data model,
infrastructure provider, primary language/framework choice.
→ Requires full protocol. Do not rush.

**Type 2 (two-way door):** Internal module boundaries, library choices, config
format, naming conventions, internal API between your own services.
→ Run abbreviated protocol (Steps 2 and 5 only). Decide fast, iterate.

## STEP 2 — Map what exists

Before designing anything new, understand what's already there:
- What components exist today?
- What are the current boundaries? (services, modules, packages)
- Where are the current pain points? (coupling, bottlenecks, tech debt)
- What constraints does the existing system impose on new design?

If greenfield, state that and skip to Step 3.

## STEP 3 — Evaluate build vs buy vs adopt

For each major component:

| Question | If YES → |
|---|---|
| Does a well-maintained OSS/SaaS solution exist? | Evaluate adopting it |
| Is this a commodity capability (auth, email, storage, logging)? | Buy/adopt, don't build |
| Is this your core differentiator? | Build it — this is where your value lives |
| Will you need to customize it beyond what exists? | Build if customization > 40% |

State each: **BUILD** / **BUY** / **ADOPT**.

## STEP 4 — Boundary analysis

For every proposed module/service boundary, verify all four tests:

**Cohesion test:** "Can I describe this module's purpose in one sentence without 'and'?"
- NO → module does too many things. **Split it.**

**Coupling test:** "If I change module A's internals, does module B need to change?"
- YES → missing abstraction. **Add an interface.**

**Data ownership test:** "Does exactly one module own each piece of data?"
- NO → shared mutable state. **Assign a single owner.**

**Communication test:**

| Pattern | Appropriate when |
|---|---|
| Direct function calls | Monolith (tight coupling) |
| Events/messages | Services (loose coupling, independent deployment) |
| Shared database | **Almost always wrong** |

## STEP 5 — Spot the bottleneck

Apply **Theory of Constraints:** Which single component limits the system's overall
capacity? Everything else is irrelevant until that bottleneck is addressed.

- Where does data queue up?
- Which step is slowest?
- Which component fails first under load?

Name the bottleneck explicitly. Your architecture must address it.

## Output format

```
ARCHITECTURE ANALYSIS
├── Decision type: [Type 1 / Type 2]
├── Components: [BUILD: x, y | BUY: z | ADOPT: w]
├── Boundaries: [cohesion ✓/✗ | coupling ✓/✗ | data ownership ✓/✗]
├── Bottleneck: [identified component and why]
├── Key risk: [the one thing most likely to require rework]
└── Confidence: [HIGH / MEDIUM / LOW]
```

## HARD-GATE

For **Type 1 decisions:** Do NOT proceed to implementation planning until all 5
steps are complete and the user has confirmed the architecture.

Type 1 decisions with MEDIUM or LOW confidence require explicit human sign-off.

## Handoff

After architecture analysis is complete and user confirms:

Proceed to `development/plan` for implementation planning. Pass your build/buy/adopt
classifications, boundary analysis, and bottleneck as context.

## Rationalization catching

STOP if you catch yourself thinking:
- "It's just an internal module" — Internal modules become public contracts.
- "We can refactor later" — Data models and API contracts cannot be refactored without migrations.
- "This is a small change" — Small changes with wrong boundaries compound.
- "I already know the architecture" — The skill ensures you verified it.