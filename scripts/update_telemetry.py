#!/usr/bin/env python3
"""
Telemetry & Metric Sync Script
Fetches live GitHub telemetry from public endpoints or GitHub CLI and updates
profile metadata.
"""

import json
import os
import subprocess
import sys
import urllib.request

USERNAME = "Ju1iaN-Zhang"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def fetch_github_user_data(username):
    """Fetches user public profile data from GitHub API."""
    url = f"https://api.github.com/users/{username}"
    headers = {"User-Agent": "GitHub-Profile-Sync"}
    
    # Try using gh CLI if available
    try:
        res = subprocess.run(["gh", "api", f"users/{username}"], capture_output=True, text=True)
        if res.returncode == 0:
            return json.loads(res.stdout)
    except Exception:
        pass

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Warning: Could not fetch remote user data: {e}", file=sys.stderr)
        return {
            "login": username,
            "public_repos": 2,
            "followers": 1,
            "following": 0,
            "bio": "看过最好的才能更通透"
        }

def fetch_user_repos(username):
    """Fetches user repositories from GitHub."""
    try:
        res = subprocess.run(["gh", "api", f"users/{username}/repos?per_page=100"], capture_output=True, text=True)
        if res.returncode == 0:
            return json.loads(res.stdout)
    except Exception:
        pass

    url = f"https://api.github.com/users/{username}/repos?per_page=100"
    headers = {"User-Agent": "GitHub-Profile-Sync"}
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Warning: Could not fetch repo list: {e}", file=sys.stderr)
        return []

def generate_telemetry_report():
    user = fetch_github_user_data(USERNAME)
    repos = fetch_user_repos(USERNAME)
    
    total_stars = sum(r.get("stargazers_count", 0) for r in repos)
    total_forks = sum(r.get("forks_count", 0) for r in repos)
    languages = set(r.get("language") for r in repos if r.get("language"))
    
    report = {
        "user": user.get("login", USERNAME),
        "bio": user.get("bio", ""),
        "public_repos": user.get("public_repos", len(repos)),
        "total_stars": total_stars,
        "total_forks": total_forks,
        "active_languages": sorted(list(languages)),
        "system_status": "ONLINE"
    }
    
    telemetry_path = os.path.join(BASE_DIR, "assets", "telemetry.json")
    with open(telemetry_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"Telemetry saved to {telemetry_path}")
    print(f"User: {report['user']} | Repos: {report['public_repos']} | Stars: {report['total_stars']}")

if __name__ == "__main__":
    generate_telemetry_report()
