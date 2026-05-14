---
name: praxis-code-quality-analysis
description: >
  MANDATORY code review protocol. Invoke when writing significant code (not one-liners),
  reviewing PRs or diffs, refactoring modules, or when code quality is requested.
  Runs 15 structural checks across readability, structure, safety, purity, and design.
  Do NOT ship code with 3+ safety failures without remediation.
version: 1.0.0
author: ether-btc (ported from xD4O/praxis)
license: MIT
metadata:
  hermes:
    tags: [reasoning, code-quality, code-review, mandatory]
    related_skills: [praxis-problem-classification, praxis-security-reasoning]
---

# Code Quality Analysis Protocol

> **MANDATORY — Tests verify that code WORKS. This verifies that code is WELL-DESIGNED.**

## THE 15 CHECKS

Work through each. Mark PASS, FAIL, or N/A.

### Readability

**1. NAMING** — Does every name reveal its intent?
- `processData()` → FAIL. `extractValidEmails()` → PASS.
- Booleans read as questions: `isValid`, `hasPermission`, `canExecute`.

**2. FUNCTION SIZE** — Is every function under 20 lines?
- If over 20 lines, it does more than one thing. Extract methods.

**3. NESTING DEPTH** — Is anything nested deeper than 2 levels?
- If yes, flatten with guard clauses. Return early for invalid cases.

### Structure

**4. SINGLE RESPONSIBILITY** — Does each module have exactly one reason to change?

**5. COUPLING** — Can you change module A without touching module B?
- Count the imports. More imports = more coupling.

**6. COHESION** — Is everything inside this module related to the same concern?

### Safety

**7. FAIL FAST** — Do errors surface immediately with clear messages?
- No empty catch blocks. No silently defaulting to zero/null/empty on bad input.

**8. IDEMPOTENCY** — What happens if this operation runs twice?

**9. INPUT VALIDATION** — Are all inputs validated at the boundary?

### Purity

**10. COMMAND-QUERY SEPARATION** — Does every function either return data OR change state?

**11. IMMUTABILITY** — Is data mutated, or are new copies created?

**12. SURPRISE CHECK** — Would a reader be surprised by ANY behavior?

### Design

**13. COMPOSITION** — Is inheritance used where composition would work?
- "Has-a" is almost always better than "is-a."

**14. ORTHOGONALITY** — If you change feature X, how many other files change?
- Ideal: 1. If more than 3 files change, there's an abstraction boundary missing.

**15. SIMPLICITY** — Is this the simplest approach?
- Any feature built for "maybe someday"? Delete it (YAGNI).

## Output format

```
CODE QUALITY ANALYSIS
├── Readability:  Naming [P/F] | Size [P/F] | Nesting [P/F]
├── Structure:    SRP [P/F] | Coupling [P/F] | Cohesion [P/F]
├── Safety:       FailFast [P/F] | Idempotent [P/F] | Validation [P/F]
├── Purity:       CQS [P/F] | Immutable [P/F] | NoSurprise [P/F]
├── Design:       Composition [P/F] | Orthogonal [P/F] | Simple [P/F]
├── Score:        [X/15 passed]
└── Action items: [list any FAIL items with specific fix]
```

## HARD-GATE

Code with **3+ FAIL items in Safety or Structure** categories should not ship
without remediation. Flag these as blocking issues.

## Handoff

After the 15-check analysis is complete:

Present the report with specific fix recommendations for each FAIL item.
Safety and Structure FAILs are blocking items.

## Rationalization catching

STOP if you catch yourself thinking:
- "It works" — Working is the minimum bar. Well-designed is the standard.
- "We'll refactor later" — Later never comes. Fix it now.
- "It's just a prototype" — Prototypes become production. Build the habit.
- "The tests pass" — Tests verify behavior, not design quality. Both matter.