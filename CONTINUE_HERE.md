# Praxis Hermes Port — CONTINUE_HERE

## What was accomplished

**Goal:** Make ether-btc/praxis usable as Hermes Agent skills.

### Research findings
- Praxis was a Claude Code plugin (xD4O/praxis original, ether-btc/praxis fork)
- Incompatible with Hermes: used Claude Code SessionStart hooks, `find ~/.claude` paths, `Skill(superpowers:)` invocations
- Previous sessions had done an audit+fix of the repo (commands namespace, repo refs, rationalization catching) but no Hermes port

### Solution: Hermes port

Converted all 9 skills from Claude Code plugin format to standalone Hermes SKILL.md files:

**Root meta-skill:** `praxis` at `~/.hermes/skills/praxis/SKILL.md`
- Routes to sub-skills based on problem type
- Complexity gate (trivial skip, non-trivial invoke)
- Execution chain diagram

**9 sub-skills** (flat naming, e.g. `praxis-problem-classification`):
1. `praxis-problem-classification` — 4-gate framing (NEW-BUILD/EXTEND/FIX/OPTIMIZE/DECIDE/ANALYZE)
2. `praxis-architecture-reasoning` — reversibility classification, build/buy/adopt, boundary analysis, bottleneck ID
3. `praxis-security-reasoning` — STRIDE per trust boundary
4. `praxis-decision-analysis` — weighted criteria, expected value, second-order, pre-mortem, steelman
5. `praxis-diagnostic-reasoning` — 5 hypotheses, Strong Inference discriminating test, 5 Whys
6. `praxis-code-quality-analysis` — 15 checks (readability, structure, safety, purity, design)
7. `praxis-gap-analysis` — 7 cognitive debiasing checks (inversion, second-order, MECE, map vs territory, adversarial, simplicity, reversibility)
8. `praxis-strategic-reasoning` — SWOT, competitive landscape, impact/effort matrix, OKRs
9. `praxis-architecture-reasoning` (already listed) — duplicate skip, actual #9 is the using-praxis which is the root

**Key design decisions:**
- Flat skill names (praxis-*) used because Hermes resolves by `name:` frontmatter field, not directory path
- All Claude Code specifics removed: `find ~/.claude` → `skill_view(name='praxis-...')`, Superpowers → `development/plan`
- `<HARD-GATE>` and `<RATIONALIZATION-CATCHING>` tags converted to plain text sections

### Files committed and pushed

**In repo** (`~/projects/praxis/`):
- `HERMES_PORT.md` — full documentation of the Hermes adaptation
- `hermes-skills/` — the 9 Hermes SKILL.md files (copied from `~/.hermes/skills/`)
- `SKILL.md` (updated) — added Hermes port reference

**Already installed locally** (`~/.hermes/skills/`):
- `praxis/SKILL.md` (root meta-skill)
- `praxis-problem-classification/SKILL.md`
- `praxis-architecture-reasoning/SKILL.md`
- `praxis-security-reasoning/SKILL.md`
- `praxis-decision-analysis/SKILL.md`
- `praxis-diagnostic-reasoning/SKILL.md`
- `praxis-code-quality-analysis/SKILL.md`
- `praxis-gap-analysis/SKILL.md`
- `praxis-strategic-reasoning/SKILL.md`

### Git
- Committed: `9ac5168` — "feat: Hermes Agent port — standalone SKILL.md files for praxis"
- Pushed to: `origin/main` (ether-btc/praxis)

## How to test

```python
# In a new session, verify skills are visible:
skill_view(name='praxis')           # should load root meta-skill
skill_view(name='praxis-problem-classification')  # should load sub-skill
skills_list()                        # should show praxis and praxis-* skills
```

## Next time

- **Use Praxis actively** — next time you encounter a non-trivial task (system design, debugging, architecture decision), invoke `skill_view(name='praxis')` first and follow the protocol
- **Verify the install method works** — `cp -r hermes-skills/* ~/.hermes/skills/` should be the install command users run
- **Consider automating install** — could add a `install-hermes.sh` script to the repo that copies the hermes-skills directory

## What could still be improved

- The skills work but haven't been tested in an actual session with a non-trivial task
- Could add a `tests/test_hermes_port.py` to verify skill loading
- Could add `install-hermes.sh` script to repo root
- Superpowers handoff was replaced with `development/plan` — if Superpowers skills become available, could add Superpowers routing back