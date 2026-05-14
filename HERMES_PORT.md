# Praxis — Hermes Agent Port

This document describes how Praxis is adapted for Hermes Agent.

## Overview

The original Praxis is a Claude Code plugin that uses SessionStart hooks and `find ~/.claude` commands. The Hermes port converts all 9 skills into standalone Hermes SKILL.md files that work with Hermes's native `skill_view` system.

## Architecture

### Hermes Skill Names

Each skill is a standalone SKILL.md file installed under `~/.hermes/skills/`:

| Skill | File | Hermes name |
|-------|------|-------------|
| Root meta-skill | `praxis/SKILL.md` | `praxis` |
| Problem classification | `praxis-problem-classification/SKILL.md` | `praxis-problem-classification` |
| Architecture reasoning | `praxis-architecture-reasoning/SKILL.md` | `praxis-architecture-reasoning` |
| Security reasoning | `praxis-security-reasoning/SKILL.md` | `praxis-security-reasoning` |
| Decision analysis | `praxis-decision-analysis/SKILL.md` | `praxis-decision-analysis` |
| Diagnostic reasoning | `praxis-diagnostic-reasoning/SKILL.md` | `praxis-diagnostic-reasoning` |
| Code quality analysis | `praxis-code-quality-analysis/SKILL.md` | `praxis-code-quality-analysis` |
| Gap analysis | `praxis-gap-analysis/SKILL.md` | `praxis-gap-analysis` |
| Strategic reasoning | `praxis-strategic-reasoning/SKILL.md` | `praxis-strategic-reasoning` |

Flat naming (instead of `praxis/problem-classification`) is used because Hermes's skill
loader resolves names by matching the `name:` field in SKILL.md frontmatter, not by
directory path. Each skill must have a unique `name:` field across the entire skills tree.

## How to Use

### 1. Install

```bash
# Clone the repo (or pull latest)
git clone https://github.com/ether-btc/praxis.git ~/projects/praxis

# Copy Hermes-ready skills to your skills directory
cp -r ~/projects/praxis/hermes-skills/* ~/.hermes/skills/

# Verify
skills_list()  # should show praxis and praxis-* skills
```

### 2. Invoke

**Start with the root meta-skill:**
```
skill_view(name='praxis')
```

**Chain to sub-skills:**
```
skill_view(name='praxis-problem-classification')
skill_view(name='praxis-gap-analysis')
```

### 3. Workflow

For non-trivial tasks:

1. `skill_view(name='praxis')` — classify the problem type and route to the right sub-skill
2. Follow the complexity gate — trivial tasks skip, non-trivial tasks invoke sub-skills
3. Invoke the matched sub-skill via `skill_view(name='praxis-<sub-skill>')`
4. Follow the sub-skill's protocol completely before responding
5. Chain to additional sub-skills if the routing table indicates more apply
6. After Praxis reasoning is complete, proceed to `development/plan` for implementation

## Hermes Integration

### Skill Chaining
Skills chain naturally via `skill_view(name='praxis-<sub-skill>')` calls — the root skill
routes to sub-skills, sub-skills chain to each other per the execution chain table.

### Handoff
After Praxis reasoning is complete:
- Design → `development/plan` for implementation planning
- Code execution → normal toolchain

### What was changed from the Claude Code version

| Original (Claude Code) | Hermes Port |
|---|---|
| `find ~/.claude -path "*/praxis/skills/..."` | `skill_view(name='praxis-<skill>')` |
| `<HARD-GATE>` tags | Hard-gate text retained, adapted to Hermes's skill format |
| `<RATIONALIZATION-CATCHING>` tags | Inline rationalization catching sections |
| SessionStart hook for auto-activation | Manual invocation via `skill_view` — Hermes skills are loaded on demand |
| `Skill(superpowers:...)` handoff | `development/plan` handoff (Superpowers-specific references removed) |
| CLAUDE.md agent instructions | Retained in repo for AI agents contributing to this repo |

## Files in this Port

```
hermes-skills/
├── SKILL.md                      ← this file (container overview)
├── praxis/                       ← root meta-skill
│   └── SKILL.md
├── praxis-problem-classification/
│   └── SKILL.md
├── praxis-architecture-reasoning/
│   └── SKILL.md
├── praxis-security-reasoning/
│   └── SKILL.md
├── praxis-decision-analysis/
│   └── SKILL.md
├── praxis-diagnostic-reasoning/
│   └── SKILL.md
├── praxis-code-quality-analysis/
│   └── SKILL.md
├── praxis-gap-analysis/
│   └── SKILL.md
└── praxis-strategic-reasoning/
    └── SKILL.md
```