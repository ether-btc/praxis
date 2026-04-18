---
name: using-praxis
description: >
  MANDATORY — HIGHEST PRIORITY SKILL. You MUST invoke this skill (praxis) BEFORE invoking
  superpowers:brainstorming or ANY other skill when the task is non-trivial. This skill
  classifies the problem, selects reasoning frameworks, and runs threat analysis BEFORE
  brainstorming begins. Do NOT invoke superpowers:brainstorming first. Do NOT respond
  directly. Do NOT ask clarifying questions on your own. Invoke praxis FIRST, complete
  its gates, THEN hand off to superpowers:brainstorming. Non-trivial means: system design,
  feature planning, architecture decisions, debugging, security-sensitive code, trade-off
  evaluation, code review, or refactoring. Trivial means: fix a typo, rename a variable,
  answer a factual question, run a command.
---

# PRAXIS Reasoning Protocol

EXTREMELY_IMPORTANT: This protocol is MANDATORY, not advisory. You do NOT have the option
to "just engage directly" or "handle this conversationally" when a non-trivial task matches
the routing table below. You MUST invoke the matching skill BEFORE you respond to the user.

<HARD-GATE>
BEFORE writing ANY response to a non-trivial user request, you MUST:

1. Classify the task against the complexity gate below
2. If non-trivial: identify the matching skill from the routing table
3. Invoke that skill using the Skill tool
4. Follow the skill's protocol completely
5. ONLY THEN respond to the user with your analysis

You are NOT ALLOWED to skip this process. You are NOT ALLOWED to "engage directly" with
a non-trivial task. You are NOT ALLOWED to decide that you can "handle this without the
skill." The skill exists because ad-hoc reasoning misses things. Every time.

If you catch yourself thinking "I can just handle this directly" or "this doesn't need
the full protocol" for a task that matches the non-trivial list — STOP. That impulse is
exactly why this gate exists. Invoke the skill.
</HARD-GATE>

## Complexity gate

**Trivial** (skip PRAXIS, respond directly):
Fix a typo. Rename a variable. Answer a factual question. Run a command. Write a one-liner.
Format something. Explain syntax. Simple file edits. Git operations. Package installs.

**Non-trivial** (MUST invoke matching skill BEFORE responding):
Design a system or feature. Debug a complex issue. Make an architecture decision. Evaluate
trade-offs. Write security-sensitive code. Refactor significant code. Plan a feature. Review
an approach or design. Choose between alternatives. Analyze a failure or incident. Build
anything with auth, payments, or user data.

If unsure whether trivial or non-trivial: invoke the skill. False positives cost 30 seconds
of structured thinking. False negatives cost hours of rework from a bad approach.

## Skill routing

When a non-trivial task arrives, invoke the FIRST matching skill from this table:

| The task involves | READ THIS SUB-PROTOCOL |
|---|---|
| Starting any new design or feature | `problem-classification/SKILL.md` |
| Architecture, module boundaries, build-vs-buy | `architecture-reasoning/SKILL.md` |
| Authentication, authorization, crypto, input handling | `security-reasoning/SKILL.md` |
| Choosing between options, trade-offs, priorities | `decision-analysis/SKILL.md` |
| Debugging, investigating, diagnosing failures | `diagnostic-reasoning/SKILL.md` |
| Writing, reviewing, or refactoring significant code | `code-quality-analysis/SKILL.md` |
| Finalizing any design, plan, or recommendation | `gap-analysis/SKILL.md` |
| Business strategy, market positioning, OKRs | `strategic-reasoning/SKILL.md` |

To load a sub-protocol, run: `find ~/.claude -path "*/praxis/skills/[name]/SKILL.md" -exec cat {} \;`
Then follow it completely before responding to the user.

If multiple rows match, invoke the FIRST match. Skills can chain — after completing one,
check if another applies to the result.

## How to invoke sub-protocols

The Skill tool loaded this meta-skill. To load a specific sub-protocol, find and read
its SKILL.md file. Use bash:

```
find ~/.claude -path "*/praxis/skills/[skill-name]/SKILL.md" -exec cat {} \;
```

For example, for problem-classification:
```
find ~/.claude -path "*/praxis/skills/problem-classification/SKILL.md" -exec cat {} \;
```

If that doesn't work, try: `cat "$(dirname "$(find ~/.claude -name 'using-praxis' -type d)")/problem-classification/SKILL.md"`

After reading the sub-protocol, follow it step by step as written. Do not summarize.
Do not skip steps. Do not paraphrase. Execute each gate in order.

## Confidence reporting

Every PRAXIS analysis MUST end with a confidence assessment:

- **HIGH (90%+):** Multiple independent checks passed. You would bet your job on this.
- **MEDIUM (70-89%):** Reasoning is sound but has unverified assumptions. List them.
- **LOW (50-69%):** Significant uncertainty. State what information would raise confidence.
- **INSUFFICIENT (<50%):** Cannot make a reliable recommendation. Escalate to human.

## Superpowers handoff (MANDATORY when Superpowers is installed)

Check if Superpowers skills are available by running: `Skill(superpowers)`
If Superpowers is installed, you MUST hand off to it at these specific moments.
Do NOT let PRAXIS own the entire conversation. PRAXIS reasons. Superpowers executes.

### Handoff sequence

After completing `problem-classification` and gathering user constraints:
→ Invoke `Skill(superpowers:brainstorming)` and pass your classification, frameworks,
  and constraints as context. Let Superpowers drive the design conversation.
  Do NOT continue designing inside PRAXIS. Hand off NOW.

After Superpowers brainstorming produces a design:
→ Invoke PRAXIS `gap-analysis` (read the sub-protocol via bash). Run the 7 checks
  against the design Superpowers produced. Report findings to the user.

After gap-analysis approves the design:
→ Invoke `Skill(superpowers:writing-plans)` to create the implementation plan.
  Do NOT write the plan inside PRAXIS. Hand off NOW.

During implementation (Superpowers handles TDD/subagents):
→ PRAXIS stays quiet. Let Superpowers execute.

When Superpowers triggers code review:
→ PRAXIS `code-quality-analysis` and `security-reasoning` augment the review.
  Run both, then let Superpowers' code-reviewer agent finalize.

When debugging:
→ PRAXIS `diagnostic-reasoning` runs first (5 hypotheses, discriminating test).
  Then invoke `Skill(superpowers:systematic-debugging)` to execute the investigation.

### The rule

Never let PRAXIS replace Superpowers. PRAXIS adds reasoning THEN hands off.
If you find yourself doing brainstorming, plan-writing, or code execution inside
PRAXIS when Superpowers is available — STOP. You are supposed to hand off.
PRAXIS thinks. Superpowers does.

<RATIONALIZATION-CATCHING>
If you find yourself thinking any of these, you are about to violate the protocol:

- "I can handle this directly" — No. Invoke the skill.
- "This is straightforward enough" — If it matched the non-trivial list, invoke the skill.
- "The user wants a quick answer" — A 30-second skill invocation prevents a 2-week mistake.
- "I already know the right approach" — The skill catches what confidence alone misses.
- "Let me just ask clarifying questions first" — The skill's gates ARE the clarifying questions.
- "This doesn't need the full protocol" — You don't get to decide that. The gate does.
</RATIONALIZATION-CATCHING>
