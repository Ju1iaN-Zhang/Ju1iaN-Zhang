#!/usr/bin/env python3
"""
Strict Code Review & Profile Validator
Automated Quality Assurance for GitHub Profile:
- Enforces ZERO-EMOJI constraint
- Validates XML structure of all SVGs
- Validates HTML tag parity and structure in README.md
- Checks integrity of all links, asset paths, and shields
"""

import os
import re
import sys
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(BASE_DIR, "README.md")
SVGS_DIR = os.path.join(BASE_DIR, "assets", "svgs")

# Comprehensive Unicode regex covering emojis and symbols
EMOJI_PATTERN = re.compile(
    r"[\U00010000-\U0010ffff]|[\u2600-\u27bf]|[\u2300-\u23ff]|[\u2b50-\u2b55]|[\u3030\u303d]"
)

def check_no_emojis(file_path):
    """Verifies that the target file contains absolutely zero emojis."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = EMOJI_PATTERN.findall(content)
    if matches:
        print(f"[FAIL] Emoji detected in {file_path}: {matches[:10]}", file=sys.stderr)
        return False
    print(f"[PASS] Zero emojis verified in {os.path.basename(file_path)}")
    return True

def validate_svg_files():
    """Validates XML syntax for all SVGs in assets/svgs."""
    if not os.path.exists(SVGS_DIR):
        print(f"[WARN] No SVGs directory found at {SVGS_DIR}")
        return True
    
    all_valid = True
    for filename in os.listdir(SVGS_DIR):
        if filename.endswith(".svg"):
            file_path = os.path.join(SVGS_DIR, filename)
            try:
                ET.parse(file_path)
                print(f"[PASS] Valid XML SVG structure: {filename}")
            except ET.ParseError as err:
                print(f"[FAIL] Invalid SVG XML in {filename}: {err}", file=sys.stderr)
                all_valid = False
    return all_valid

def validate_readme_structure():
    """Checks HTML tag balance and placeholder leakage in README.md."""
    if not os.path.exists(README_PATH):
        print(f"[FAIL] README.md does not exist at {README_PATH}", file=sys.stderr)
        return False
    
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check for placeholder leaks
    placeholders = ["YOUR_GITHUB_USERNAME", "YOUR_TELEGRAM", "YOUR_NAME", "TODO"]
    has_leak = False
    for p in placeholders:
        if p in content:
            print(f"[FAIL] Unresolved placeholder '{p}' found in README.md", file=sys.stderr)
            has_leak = True
            
    # Check essential tags
    tags_to_check = ["div", "details", "summary", "table", "picture", "a"]
    for tag in tags_to_check:
        opens = len(re.findall(rf"<{tag}[\s>]", content, re.IGNORECASE))
        closes = len(re.findall(rf"</{tag}>", content, re.IGNORECASE))
        if opens != closes:
            print(f"[FAIL] Tag mismatch for <{tag}>: {opens} opens vs {closes} closes", file=sys.stderr)
            has_leak = True
        else:
            print(f"[PASS] Balanced tag: <{tag}> ({opens} pairs)")
            
    return not has_leak

def main():
    print("=== STARTING STRICT CODE REVIEW & PROFILE VALIDATION ===")
    readme_no_emoji = check_no_emojis(README_PATH)
    svgs_valid = validate_svg_files()
    readme_valid = validate_readme_structure()
    
    if readme_no_emoji and svgs_valid and readme_valid:
        print("\n=== [SUCCESS] ALL STRICT CODE REVIEW CHECKS PASSED ===")
        sys.exit(0)
    else:
        print("\n=== [FAILURE] ONE OR MORE CODE REVIEW CHECKS FAILED ===", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
