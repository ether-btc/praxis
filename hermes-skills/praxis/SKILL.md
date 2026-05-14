---
name: praxis
description: >
  Use when the user presents a non-trivial task — system design, debugging, architecture
  decisions, security-sensitive code, trade-off evaluation, code review, or refactoring.
  This is the ROOT META-SKILL that classifies the problem type and routes to the correct
  sub-skill BEFORE any other action. Load this FIRST, then chain to the appropriate
  sub-skill. Do NOT respond directly to non-trivial requests without running this protocol.
version: 1.0.0
author: ether-btc (ported from xD4O/praxis)
license: MIT
metadata:
  hermes:
    tags: [reasoning, protocol, meta-skill, decision-making, analysis]
    related_skills: [development/plan, development/hierarchical-code-analysis]
---

# Praxis — Reasoning Protocol (Hermes Edition)

> **MANDATORY — HIGHEST PRIORITY SKILL.** You MUST invoke this skill BEFORE any other
> action on non-trivial tasks.

Praxis classifies problems, selects reasoning frameworks, and runs analysis **BEFORE**
brainstorming or execution begins.

---

## Complexity Gate

### Trivial → skip, respond directly
- Fix a typo, rename a variable, answer a factual question
- Run a command, write a one-liner, format something
- Explain syntax, simple file edits, git operations, package installs

### Non-trivial → MUST invoke matching sub-skill FIRST
- Design a system or feature
- Debug a complex issue
- Make an architecture decision
- Evaluate trade-offs
- Write security-sensitive code
- Refactor significant code
- Plan a feature
- Review an approach or design
- Choose between alternatives
- Analyze a failure or incident
- Build anything with auth, payments, or user data

> If unsure: **invoke the skill**. False positive = 30 seconds. False negative = hours of rework.

---

## Skill Routing Table

| The task involves | Invoke this sub-skill |
|---|---|
| Starting any new design or feature | `praxis-problem-classification` |
| Architecture, module boundaries, build-vs-buy | `praxis-architecture-reasoning` |
| Authentication, authorization, crypto, input handling | `praxis-security-reasoning` |
| Choosing between options, trade-offs, priorities | `praxis-decision-analysis` |
| Debugging, investigating, diagnosing failures | `praxis-diagnostic-reasoning` |
| Writing, reviewing, or refactoring significant code | `praxis-code-quality-analysis` |
| Finalizing any design, plan, or recommendation | `praxis-gap-analysis` |
| Business strategy, market positioning, OKRs | `praxis-strategic-reasoning` |

> To invoke a sub-skill: `skill_view(name='praxis-<sub-skill>')` then follow its protocol.

---

## Execution Chain

```
user request
    └── praxis (this skill)     ← classify + route
          └── problem-classification  ← ALWAYS second (frame the problem)
                ├── [architectural] → architecture-reasoning
                ├── [code quality]  → code-quality-analysis
                ├── [trade-off]     → decision-analysis
                ├── [debugging]     → diagnostic-reasoning
                ├── [design review] → gap-analysis
                ├── [security]      → security-reasoning
                └── [business]      → strategic-reasoning
```

---

## Confidence Reporting

Every Praxis analysis **MUST** end with a confidence assessment:

| Level | Range | Criteria |
|---|---|---|
| **HIGH** | 90%+ | Multiple independent checks passed |
| **MEDIUM** | 70–89% | Sound but has unverified assumptions — **list them** |
| **LOW** | 50–69% | Significant uncertainty — **state what raises it** |
| **INSUFFICIENT** | <50% | Cannot make a recommendation — **escalate to human** |

---

## Hermes Integration Notes

### Handoff
After Praxis reasoning is complete, hand off to execution skills:
- Design exploration → `development/plan` for implementation planning
- Code writing → proceed with your normal toolchain

### Chain Rule
Skills can chain — after completing one, re-check the routing table. If another applies
to the result, invoke it before responding to the user.

### What Praxis is NOT
- A reference document — it's a behavioral protocol with mandatory gates
- Optional — gates exist precisely because "I'll just handle it directly" fails
- A brainstorming tool — it runs BEFORE brainstorming, not during

---

## Warning Signs — STOP if you catch yourself thinking

- [ ] * "I can handle this directly" → No. Invoke the skill.
- [ ] * "This is straightforward enough" → If it matched the non-trivial list, invoke.
- [ ] * "The user wants a quick answer" → A 30-second invocation prevents a 2-week mistake.
- [ ] * "I already know the right approach" → The skill catches what confidence alone misses.
- [ ] * "Let me just ask clarifying questions first" → The skill's gates ARE the questions.