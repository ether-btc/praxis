---
name: security-reasoning
description: >
  MANDATORY threat analysis. You MUST invoke this skill before writing or approving ANY
  code involving authentication, authorization, cryptography, input handling, payment
  processing, PII, secrets management, API endpoints, or trust boundaries. Do NOT write
  security-sensitive code without running STRIDE analysis first. Do NOT say you will add
  security later. Auth is a design decision, not a feature to bolt on.
---

# Security Reasoning Protocol

EXTREMELY_IMPORTANT: This is a MANDATORY protocol, not a suggestion. Follow every step.
Do not skip steps. Do not combine steps. Do not summarize. Work through each gate in order.

This task involves a trust boundary. You MUST complete threat analysis before writing
or approving security-sensitive code.

## STEP 1 — Identify trust boundaries

List every point where data crosses a trust boundary:
- User input entering the system
- Data crossing network boundaries
- Calls between services with different privilege levels
- Data entering or leaving storage
- Interactions with third-party services

For each boundary, name what's on each side and what data crosses.

## STEP 2 — STRIDE analysis

For each trust boundary, answer ALL six questions. Do not skip any.
Mark each as MITIGATED, NEEDS-MITIGATION, or NOT-APPLICABLE.

**S — Spoofing:** Can an attacker pretend to be someone else at this boundary?
How is identity verified? What happens if verification is bypassed?

**T — Tampering:** Can data be modified in transit or at rest?
Is integrity checked? What happens if data is silently corrupted?

**R — Repudiation:** Can a user deny they performed an action?
Are significant actions audit-logged with tamper-proof timestamps?

**I — Information Disclosure:** Can sensitive data leak?
Is data encrypted in transit (TLS) and at rest? Are error messages sanitized?
Do logs accidentally include tokens, passwords, or PII?

**D — Denial of Service:** Can this boundary be overwhelmed?
Is there rate limiting? Resource quotas? Timeout enforcement?

**E — Elevation of Privilege:** Can a user gain unauthorized access?
Is authorization checked at every operation, not just at the entry point?
Are permissions enforced server-side, not just client-side?

## STEP 3 — Attack surface summary

Produce a table:

| Boundary | Threat | Severity | Mitigation | Status |
|---|---|---|---|---|
| [boundary] | [S/T/R/I/D/E] | [Critical/High/Med/Low] | [what prevents it] | [done/needed] |

## STEP 4 — Top 3 risks

From the table, identify the 3 highest-severity unmitigated threats.
For each, state the specific mitigation required before this code ships.

## Output format

```
SECURITY ANALYSIS
├── Trust boundaries: [list of boundaries identified]
├── Attack surface:
│   ├── [Boundary 1]: [S/T/R/I/D/E] → [mitigation status]
│   ├── [Boundary 2]: [S/T/R/I/D/E] → [mitigation status]
│   └── ...
├── Top 3 risks:
│   1. [Risk] → [specific mitigation required]
│   2. [Risk] → [specific mitigation required]
│   3. [Risk] → [specific mitigation required]
└── Confidence: [HIGH / MEDIUM / LOW]
```

<HARD-GATE>
Do NOT approve, merge, or present security-sensitive code as complete until:
- All trust boundaries are identified
- STRIDE is answered for each boundary (no blanks)
- Top 3 risks have specific mitigations
</HARD-GATE>

## Superpowers handoff

After STRIDE analysis is complete and mitigations are identified:

If Superpowers is installed → pass the threat model and required mitigations to whichever
Superpowers skill is active (brainstorming, writing-plans, or code-review). The mitigations
MUST appear in the plan and be verified during code review. Do NOT implement security
mitigations inside this skill — hand the requirements to Superpowers for execution.

If Superpowers is NOT installed → proceed to implementation with the mitigations as
requirements in your own plan.

<RATIONALIZATION-CATCHING>
If you find yourself thinking any of these, you are about to violate the protocol:

- "We'll add auth later" — NO. Auth is a design decision, not a feature.
- "It's internal only" — Internal networks get compromised. Defense in depth.
- "The framework handles it" — WHICH framework feature? Is it enabled? Configured?
- "We validate on the client" — Client validation is UX. Server validation is security.
- "We don't handle payments" — STRIDE applies to all trust boundaries, not just payments.
- "This is a small internal script" — Security applies to all code with trust boundaries.
</RATIONALIZATION-CATCHING>
