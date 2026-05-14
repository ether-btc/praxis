---
name: praxis-problem-classification
description: >
  MANDATORY first step. Invoke before brainstorming, designing, or planning any non-trivial
  work. This skill's gates ARE the clarifying questions — do not ask your own. Invoke when
  the user asks to build, design, plan, create, architect, or implement anything substantial.
version: 1.0.0
author: ether-btc (ported from xD4O/praxis)
license: MIT
metadata:
  hermes:
    tags: [reasoning, problem-classification, analysis, mandatory]
    related_skills: [praxis-architecture-reasoning, praxis-gap-analysis]
---

# Problem Classification Protocol

> **MANDATORY — Do not skip steps. Do not combine. Do not summarize.**

## GATE 1 — Name the problem type

Classify as **exactly ONE**:

| Type | Signature | Example |
|---|---|---|
| **NEW-BUILD** | Creating something that doesn't exist | "Build a notification service" |
| **EXTEND** | Adding capability to something that exists | "Add OAuth to our API" |
| **FIX** | Something is broken or wrong | "API returns 500 intermittently" |
| **OPTIMIZE** | Something works but needs to be better | "Reduce query latency from 800ms" |
| **DECIDE** | Choosing between alternatives | "Monolith vs microservices?" |
| **ANALYZE** | Understanding something to assess it | "Is our auth implementation secure?" |

State explicitly: "This is a **[TYPE]** problem."

## GATE 2 — Identify the constraint envelope

List hard constraints. Ask the user if unclear. Do not invent constraints.

- **Time:** Deadline? Urgency?
- **Scope:** What's in and out of bounds?
- **Resources:** Tools, languages, infrastructure available?
- **Quality:** Failure tolerance — prototype vs production vs safety-critical?
- **Dependencies:** What existing systems must this integrate with?

If the user hasn't specified a constraint, **ask**. Do not assume.

## GATE 3 — Select reasoning frameworks

Select **2-3 frameworks maximum** based on problem type:

| Problem type | Primary framework | Supporting frameworks |
|---|---|---|
| NEW-BUILD | First Principles | Constraint-Driven Design, TRIZ |
| EXTEND | Separation of Concerns | Cohesion/Coupling, Backward Compatibility |
| FIX | Abductive Reasoning | Strong Inference, 5 Whys |
| OPTIMIZE | Theory of Constraints | Pareto (80/20), Measurement-First |
| DECIDE | Expected Value Analysis | Reversibility Test, Second-Order Thinking |
| ANALYZE | STRIDE + MECE | Inversion, Red Team |

State explicitly: "Selected frameworks: [X], [Y], [Z]."
State one sentence for WHY each framework fits this specific problem.

## GATE 4 — Frame the approach

In 3-5 sentences:
1. What the problem **actually is** (not what the user said)
2. What approach you'll take and why
3. What the first question you need answered is

Present this to the user. Get confirmation before proceeding.

## HARD-GATE

Do NOT proceed to brainstorming, design, or implementation until:
- Problem type is named
- Constraints are enumerated (or confirmed unconstrained)
- Frameworks are selected with justification
- User has confirmed the approach framing

## Output format

```
PROBLEM CLASSIFICATION
├── Type: [NEW-BUILD / EXTEND / FIX / OPTIMIZE / DECIDE / ANALYZE]
├── Constraints: [enumerated or confirmed unconstrained]
├── Frameworks: [primary] + [supporting] — [one-sentence justification each]
├── Approach: [3-5 sentence framing of the real problem]
└── Confidence: [HIGH / MEDIUM / LOW / INSUFFICIENT]
```

## Handoff

After all 4 gates are complete and the user has confirmed the approach:

Proceed to `development/plan` for implementation planning, passing your problem type,
frameworks, and constraints as context.

## Rationalization catching

STOP if you catch yourself thinking:
- "I can handle this directly" — The skill's gates ARE the clarifying questions.
- "This is straightforward" — Straightforward-seeming tasks with wrong framing
  produce the most expensive failures.
- "Let me just ask clarifying questions" — The skill's gates ARE the clarifying questions.
- "I already know the problem type" — The skill ensures you classified it, not assumed.
- "The user is in a hurry" — A 2-minute classification prevents a 2-week rework.