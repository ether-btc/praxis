---
name: praxis-diagnostic-reasoning
description: >
  MANDATORY debugging protocol. Invoke when debugging complex issues, investigating
  failures, diagnosing intermittent problems, or performing root cause analysis.
  Do NOT start changing code before collecting observations. Do NOT guess at causes —
  generate 5 competing hypotheses and design a discriminating test. Invoke BEFORE
  touching any code when something is broken.
version: 1.0.0
author: ether-btc (ported from xD4O/praxis)
license: MIT
metadata:
  hermes:
    tags: [reasoning, debugging, diagnostics, mandatory]
    related_skills: [praxis-problem-classification, praxis-gap-analysis]
---

# Diagnostic Reasoning Protocol

> **MANDATORY — Something is broken. Do NOT start changing code. Follow this protocol.**

## PHASE 1 — Observe precisely

Before forming any hypothesis, collect facts:
- **What exactly happened?** (exact error, exact behavior, exact output)
- **When did it start?** (timestamp, deploy, config change, load change)
- **How often?** (every time, intermittent, under specific conditions)
- **What changed recently?** (deploys, config, dependencies, traffic patterns)
- **What's the blast radius?** (all users, some users, one endpoint, one region)

Do NOT proceed until you can state the problem in one precise sentence.

## PHASE 2 — Generate competing hypotheses

Produce exactly **5 hypotheses**. Not 1. Not 3. Five.

For each hypothesis, state:
- What it would explain
- What it would NOT explain
- Prior probability estimate (likely / possible / unlikely)

Order by: (explanatory power) × (prior probability), highest first.

**Mandatory check:** Is your #1 hypothesis the simplest explanation?
Simple causes first: config error, permissions, missing dependency, wrong
environment, typo. Check these before investigating race conditions.

## PHASE 3 — Design a discriminating test

Do NOT test hypotheses one by one. Design a single observation that
distinguishes between your top 3 hypotheses simultaneously.

Template: "If I observe [X], then hypothesis A is supported.
If I observe [Y], then hypothesis B is supported.
If I observe [Z], then hypothesis C is supported."

This is **Strong Inference.** One test, maximum information.

## PHASE 4 — Execute and update

Run the test. Observe the result.
- Which hypotheses are eliminated?
- Which are supported?
- Does the result suggest a NEW hypothesis?

Update your ranking. If top hypothesis is >80% likely, proceed to verification.
If not, return to Phase 3.

## PHASE 5 — Root cause drilling (5 Whys)

You found WHAT is broken. Now find WHY.

Ask "Why?" five times minimum, drilling to a **systemic cause**
(process, tooling, policy) rather than an individual cause.

## PHASE 6 — Verify the fix

After applying the fix:
- Does the original symptom disappear?
- Does the discriminating test now show healthy behavior?
- Are there related symptoms that should also be checked?
- What prevents this from recurring?

## Output format

```
DIAGNOSTIC ANALYSIS
├── Problem: [precise one-sentence description]
├── Hypotheses: [H1/H2/H3/H4/H5 ranked by explanatory power × prior]
├── Discriminating test: [single test that distinguishes top hypotheses]
├── Result: [which hypotheses survive]
├── Root cause: [5 Whys chain — systemic cause, not individual mistake]
├── Fix: [specific change that addresses root cause]
└── Confidence: [HIGH / MEDIUM / LOW / INSUFFICIENT]
```

## HARD-GATE

Do NOT declare an issue fixed until:
- Root cause is identified (not just the symptom patched)
- Fix is verified against original observation
- Recurrence prevention is in place or documented

## Handoff

After root cause is identified and fix is designed:

Implement the fix with your standard toolchain. Ideally: write a test that reproduces
the root cause, verify it fails, then fix (TDD pattern).

## Rationalization catching

STOP if you catch yourself thinking:
- "I think it might be..." — Generate 5 hypotheses, not 1 guess.
- "I already know the cause" — The skill ensures you verified it, not assumed.
- "Changing code before collecting observations" — Observe first. Always.
- "Testing hypotheses sequentially" — Use Strong Inference to test simultaneously.
- "Fixed!" after patching the symptom — Did you drill to root cause?