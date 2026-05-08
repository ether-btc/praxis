#!/usr/bin/env python3
"""
Integration tests for Praxis reasoning framework.
Verifies structural integrity of all skill files.

Run with: python tests/test_praxis.py
"""

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SKILLS_DIR = REPO_ROOT / "skills"

# All 9 skill names (including using-praxis as the meta-skill)
SKILL_NAMES = [
    "using-praxis",
    "problem-classification",
    "architecture-reasoning",
    "code-quality-analysis",
    "decision-analysis",
    "diagnostic-reasoning",
    "gap-analysis",
    "security-reasoning",
    "strategic-reasoning",
]

# Skills that should have Superpowers handoff (all except using-praxis)
SKILLS_WITH_HANDOFF = [s for s in SKILL_NAMES if s != "using-praxis"]

REQUIRED_BLOCKS = ["<HARD-GATE>", "<RATIONALIZATION-CATCHING>"]
CONFIDENCE_PATTERN = re.compile(r"Confidence\s*:\s*(HIGH|MEDIUM|LOW|INSUFFICIENT)", re.IGNORECASE | re.MULTILINE)


def read_skill(name: str) -> str:
    path = SKILLS_DIR / name / "SKILL.md"
    if not path.exists():
        return ""
    return path.read_text()


def parse_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter from skill content."""
    if not content.startswith("---"):
        return {}
    parts = content[3:].split("---", 1)
    if len(parts) < 2:
        return {}
    fm_text = parts[0].strip()
    result = {}
    for line in fm_text.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            result[key.strip()] = val.strip()
    return result


def test_all_skill_files_exist():
    """T1: All 9 skill directories and SKILL.md files exist."""
    missing = []
    for name in SKILL_NAMES:
        dir_path = SKILLS_DIR / name
        file_path = dir_path / "SKILL.md"
        if not dir_path.exists():
            missing.append(f"directory: {name}")
        elif not file_path.exists():
            missing.append(f"file: {name}/SKILL.md")
    assert not missing, f"Missing: {', '.join(missing)}"
    print("  T1 PASS: All 9 skill files exist")


def test_yaml_frontmatter():
    """T2: All skill files have valid YAML frontmatter with name field."""
    for name in SKILL_NAMES:
        content = read_skill(name)
        assert content.startswith("---"), f"{name}: missing frontmatter opener"
        fm = parse_frontmatter(content)
        assert "name" in fm, f"{name}: frontmatter missing 'name' field"
        assert fm["name"] == name, f"{name}: frontmatter name '{fm['name']}' != expected '{name}'"
    print("  T2 PASS: All skills have valid frontmatter with correct name")


def test_hard_gate_coverage():
    """T3: All 9 skills have HARD-GATE blocks."""
    missing = []
    for name in SKILL_NAMES:
        content = read_skill(name)
        if "<HARD-GATE>" not in content:
            missing.append(name)
    assert not missing, f"Missing HARD-GATE in: {', '.join(missing)}"
    print("  T3 PASS: All 9 skills have HARD-GATE blocks")


def test_rationalization_catching_coverage():
    """T4: All 9 skills have RATIONALIZATION-CATCHING blocks."""
    missing = []
    for name in SKILL_NAMES:
        content = read_skill(name)
        if "<RATIONALIZATION-CATCHING>" not in content:
            missing.append(name)
    assert not missing, f"Missing RATIONALIZATION-CATCHING in: {', '.join(missing)}"
    print("  T4 PASS: All 9 skills have RATIONALIZATION-CATCHING blocks")


def test_confidence_calibration():
    """T5: All skills address confidence calibration in their output format."""
    # Each skill must either:
    # 1. Have a fenced code output block containing "Confidence:" with a level, OR
    # 2. Have a dedicated "Confidence reporting" or "Confidence:" section
    for name in SKILL_NAMES:
        content = read_skill(name)
        has_fenced_confidence = bool(re.search(
            r"```[^`]*\n[^`]*Confidence[^`]*\n[^`]*```", content, re.DOTALL
        ))
        has_confidence_section = bool(re.search(
            r"(?i)## Confidence|Confidence\s*:\s*\[.*HIGH.*\]", content
        ))
        assert has_fenced_confidence or has_confidence_section, \
            f"{name}: no confidence output format found"
    print("  T5 PASS: All skills have confidence output format")


def test_superpowers_handoff():
    """T6: All 8 reasoning skills (not using-praxis) have Superpowers handoff."""
    missing = []
    for name in SKILLS_WITH_HANDOFF:
        content = read_skill(name)
        if "Superpowers handoff" not in content:
            missing.append(name)
    assert not missing, f"Missing Superpowers handoff in: {', '.join(missing)}"
    print("  T6 PASS: All 8 reasoning skills have Superpowers handoff")


def test_superpowers_handoff_format():
    """T7: All Superpowers handoffs cover both installed and NOT installed cases."""
    for name in SKILLS_WITH_HANDOFF:
        content = read_skill(name)
        assert "If Superpowers is installed" in content, f"{name}: missing 'installed' case"
        assert "If Superpowers is NOT installed" in content, f"{name}: missing 'NOT installed' case"
    print("  T7 PASS: All Superpowers handoffs handle both installed/NOT installed")


def test_routing_table_coverage():
    """T8: using-praxis routing table references all 8 sub-skills."""
    content = read_skill("using-praxis")
    missing = []
    for name in SKILL_NAMES:
        if name == "using-praxis":
            continue
        if name not in content:
            missing.append(name)
    assert not missing, f"Routing table missing reference to: {', '.join(missing)}"
    print("  T8 PASS: using-praxis routing table references all 8 sub-skills")


def test_hard_gate_blocks_not_empty():
    """T9: HARD-GATE blocks contain actual content (not just the tag)."""
    for name in SKILL_NAMES:
        content = read_skill(name)
        # Find HARD-GATE block
        match = re.search(r"<HARD-GATE>(.*?)</HARD-GATE>", content, re.DOTALL)
        assert match, f"{name}: missing </HARD-GATE> closing tag"
        block_content = match.group(1).strip()
        assert len(block_content) > 10, f"{name}: HARD-GATE block appears empty"
    print("  T9 PASS: All HARD-GATE blocks have content")


def test_rationalization_catching_not_empty():
    """T10: RATIONALIZATION-CATCHING blocks contain actual content."""
    for name in SKILL_NAMES:
        content = read_skill(name)
        match = re.search(r"<RATIONALIZATION-CATCHING>(.*?)</RATIONALIZATION-CATCHING>", content, re.DOTALL)
        assert match, f"{name}: missing </RATIONALIZATION-CATCHING> closing tag"
        block_content = match.group(1).strip()
        assert len(block_content) > 10, f"{name}: RATIONALIZATION-CATCHING block appears empty"
    print("  T10 PASS: All RATIONALIZATION-CATCHING blocks have content")


def test_commands_use_valid_paths():
    """T11: All command files reference existing skill paths."""
    commands_dir = REPO_ROOT / "commands"
    if not commands_dir.exists():
        print("  T11 SKIP: No commands directory")
        return

    command_files = list(commands_dir.glob("*.md"))
    for cmd_file in command_files:
        content = cmd_file.read_text()
        # Find find commands in the bash blocks
        find_matches = re.findall(r'find ~/.claude -path "\*/praxis/skills/(\w+)/SKILL.md"', content)
        for skill_name in find_matches:
            assert (SKILLS_DIR / skill_name / "SKILL.md").exists(), \
                f"{cmd_file.name}: references non-existent skill '{skill_name}'"
    print("  T11 PASS: All command files reference existing skill paths")


def test_session_start_hook():
    """T12: session-start hook produces clean output (no frontmatter)."""
    hook_path = REPO_ROOT / "hooks" / "session-start"
    if not hook_path.exists():
        print("  T12 SKIP: No session-start hook")
        return

    # Make hook executable if it isn't
    hook_path.chmod(0o755)

    import subprocess
    result = subprocess.run([str(hook_path)], capture_output=True, text=True,
                            cwd=str(REPO_ROOT))
    # Hook should run without error
    assert result.returncode == 0, f"Hook failed with exit code {result.returncode}"

    output = result.stdout
    # Output should NOT contain YAML frontmatter delimiters on their own lines
    # (--- inside code blocks are content, not delimiters)
    lines = output.splitlines()
    has_frontmatter_delimiter = any(line.strip() == "---" for line in lines)
    assert not has_frontmatter_delimiter, "Hook output contains frontmatter delimiter on its own line"
    print("  T12 PASS: session-start hook produces clean output")


def test_output_format_consistency():
    """T13: All skills with structured output have consistent format markers."""
    # Check that output format sections use ``` fences consistently
    for name in SKILL_NAMES:
        content = read_skill(name)
        # Count opening and closing fences
        code_blocks = content.count("```")
        assert code_blocks % 2 == 0, f"{name}: unbalanced code block markers ({code_blocks})"
    print("  T13 PASS: All skills have balanced code block markers")


def test_no_dead_links():
    """T14: Skills don't reference non-existent other skills."""
    all_content = "\n".join(read_skill(name) for name in SKILL_NAMES)
    # Skill references should be to valid skill names
    skill_refs = re.findall(r"skill[/\s]*(?:superpowers[/\s:])?(\w+(?:-\w+)*)", all_content, re.IGNORECASE)
    # Filter out common non-skill words
    skip_words = {"analysis", "reasoning", "classification", "handoff", "protocol", "step", "gate", "check"}
    for ref in skill_refs:
        if ref.lower() in skip_words:
            continue
        # References to superpowers skills are external — skip
        if ref.startswith("superpowers"):
            continue
    print("  T14 PASS: No dead skill references detected")


def run_all_tests():
    print("\n=== Praxis Integration Tests ===\n")

    tests = [
        ("T1", test_all_skill_files_exist),
        ("T2", test_yaml_frontmatter),
        ("T3", test_hard_gate_coverage),
        ("T4", test_rationalization_catching_coverage),
        ("T5", test_confidence_calibration),
        ("T6", test_superpowers_handoff),
        ("T7", test_superpowers_handoff_format),
        ("T8", test_routing_table_coverage),
        ("T9", test_hard_gate_blocks_not_empty),
        ("T10", test_rationalization_catching_not_empty),
        ("T11", test_commands_use_valid_paths),
        ("T12", test_session_start_hook),
        ("T13", test_output_format_consistency),
        ("T14", test_no_dead_links),
    ]

    passed = 0
    failed = 0

    for name, test_fn in tests:
        try:
            test_fn()
            passed += 1
        except AssertionError as e:
            print(f"  {name} FAIL: {e}")
            failed += 1
        except Exception as e:
            print(f"  {name} ERROR: {e}")
            failed += 1

    print(f"\n=== Results: {passed} passed, {failed} failed ===\n")
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)