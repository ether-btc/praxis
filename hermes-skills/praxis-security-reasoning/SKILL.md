---
name: praxis-security-reasoning
description: >
  MANDATORY threat analysis. Invoke before writing ANY code involving authentication,
  authorization, cryptography, input handling, payment processing, PII, secrets management,
  API endpoints, or trust boundaries. Do NOT write security-sensitive code without running
  STRIDE analysis first. Do NOT say you will add security later.
version: 1.0.0
author: ether-btc (ported from xD4O/praxis)
license: MIT
metadata:
  hermes:
    tags: [reasoning, security, threat-analysis, mandatory]
    related_skills: [praxis-problem-classification, praxis-code-quality-analysis]
---

# Security Reasoning Protocol

> **MANDATORY — Complete threat analysis before writing security-sensitive code.**

## STEP 1 — Identify trust boundaries

List every point where data crosses a trust boundary:
- User input entering the system
- Data crossing network boundaries
- Calls between services with different privilege levels
- Data entering or leaving storage
- Interactions with third-party services

For each boundary, name what's on each side and what data crosses.

## STEP 2 — STRIDE analysis

For each trust boundary, answer ALL six. Mark each MITIGATED, NEEDS-MITIGATION, or N/A.

**S — Spoofing:** Can an attacker pretend to be someone else at this boundary?

**T — Tampering:** Can data be modified in transit or at rest?

**R — Repudiation:** Can a user deny they performed an action?

**I — Information Disclosure:** Can sensitive data leak?

**D — Denial of Service:** Can this boundary be overwhelmed?

**E — Elevation of Privilege:** Can a user gain unauthorized access?

## STEP 3 — Attack surface summary

| Boundary | Threat | Severity | Mitigation | Status |
|---|---|---|---|---|
| [boundary] | [S/T/R/I/D/E] | [Critical/High/Med/Low] | [what prevents it] | [done/needed] |

## STEP 4 — Top 3 risks

Identify the 3 highest-severity unmitigated threats.
For each, state the specific mitigation required before this code ships.

## Output format

```
SECURITY ANALYSIS
├── Trust boundaries: [list of boundaries identified]
├── Attack surface:
│   ├── [Boundary 1]: [S/T/R/I/D/E] → [mitigation status]
│   ├── [Boundary 2]: [S/T/R/I/D/E] → [mitigation status]
├── Top 3 risks:
│   1. [Risk] → [specific mitigation required]
│   2. [Risk] → [specific mitigation required]
│   3. [Risk] → [specific mitigation required]
└── Confidence: [HIGH / MEDIUM / LOW]
```

## HARD-GATE

Do NOT approve, merge, or present security-sensitive code as complete until:
- All trust boundaries are identified
- STRIDE is answered for each boundary (no blanks)
- Top 3 risks have specific mitigations

## Handoff

After STRIDE analysis is complete:

Pass the threat model and required mitigations to your code review or implementation
workflow. The mitigations MUST appear in the plan and be verified during code review.

## Rationalization catching

STOP if you catch yourself thinking:
- "We'll add auth later" — NO. Auth is a design decision, not a feature.
- "It's internal only" — Internal networks get compromised. Defense in depth.
- "The framework handles it" — WHICH framework feature? Is it enabled? Configured?
- "We validate on the client" — Client validation is UX. Server validation is security.
- "We don't handle payments" — STRIDE applies to all trust boundaries, not just payments.