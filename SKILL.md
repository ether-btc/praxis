---
name: praxis
description: Multi-agent reasoning framework with 9 mandatory protocol skills. Always invoke using-praxis first to classify the problem, then run problem-classification before brainstorming. Each protocol is a mandatory enforcement layer — not optional guidance.
version: 1.0.0
---

# Praxis — Reasoning Framework

Praxis is a layered reasoning protocol for AI agents. It enforces structured analysis before action.

## Execution Order

```
user request
    └── using-praxis          ← ALWAYS first (classifies + routes)
          └── problem-classification  ← ALWAYS second (frames the problem)
                ├── [architectural decision] → architecture-reasoning
                ├── [code quality / review] → code-quality-analysis
                ├── [trade-off / choice]    → decision-analysis
                ├── [debugging / failure]   → diagnostic-reasoning
                ├── [design / plan review]  → gap-analysis
                ├── [security / threat]     → security-reasoning
                └── [business / strategy]   → strategic-reasoning
```

## The 9 Skills

| Skill | Trigger | When to Invoke |
|-------|---------|---------------|
| `using-praxis` | Non-trivial task | ALWAYS first — classify + route |
| `problem-classification` | Build, design, plan, architect | ALWAYS second — frame before action |
| `architecture-reasoning` | Module boundaries, build-vs-buy, data models, API contracts | Before structural decisions |
| `code-quality-analysis` | Writing code, PRs, refactoring | Before shipping significant code |
| `decision-analysis` | Build-vs-buy, rewrite-vs-patch, resource allocation | Before recommending a path |
| `diagnostic-reasoning` | Debugging, failures, root cause analysis | Before touching code on a broken system |
| `gap-analysis` | Designs, plans, architecture decisions | After drafting, before irreversible action |
| `security-reasoning` | Auth, cryptography, input handling, PII, secrets | Before writing security-sensitive code |
| `strategic-reasoning` | Business decisions, product strategy, roadmap | Before WHAT-to-build decisions |

## Skill Properties

- **Mandatory, not optional**: Each skill is labeled MANDATORY — it must be invoked, not considered
- **Enforcement protocol**: Steps are imperative ("Do X"), not advisory ("Consider X")
- **HARD-GATEs**: Prevent proceeding without completing prior steps
- **Under 150 lines per skill**: If longer, it does too many things
- **Structured output**: Results are auditable
- **Confidence levels**: Every analysis output includes a confidence assessment

## Dependencies

No external dependencies. Pure reasoning protocol.

## References

- `skills/using-praxis/` — Entry point, classifier, router
- `skills/problem-classification/` — Problem framing
- `skills/architecture-reasoning/` — Structural decision analysis
- `skills/code-quality-analysis/` — Code review protocol
- `skills/decision-analysis/` — Trade-off evaluation
- `skills/diagnostic-reasoning/` — Debugging protocol
- `skills/gap-analysis/` — Validation layer
- `skills/security-reasoning/` — Threat analysis
- `skills/strategic-reasoning/` — Business/political strategy
