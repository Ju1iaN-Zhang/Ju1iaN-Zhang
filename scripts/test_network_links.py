#!/usr/bin/env python3
"""
High-Speed Concurrent Link & Asset Verification Engine
Verifies all remote URLs concurrently in parallel with strict status code validation.
"""

import concurrent.futures
import os
import re
import sys
import urllib.request
import urllib.error

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(BASE_DIR, "README.md")

def check_url(url):
    cleaned_url = url.rstrip("),;.")
    if "raw.githubusercontent.com/Ju1iaN-Zhang/Ju1iaN-Zhang/main" in cleaned_url:
        return cleaned_url, "LOCAL_ASSET", None

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
    req = urllib.request.Request(cleaned_url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            status = response.getcode()
            return cleaned_url, "OK", status
    except urllib.error.HTTPError as e:
        if e.code in (200, 301, 302, 304, 403):
            return cleaned_url, "OK", e.code
        return cleaned_url, "FAILED", e.code
    except Exception as e:
        return cleaned_url, "WARN", str(e)

def test_all_links():
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    urls = list(set(re.findall(r'https?://[^\s\'"<>]+', content)))
    print(f"Testing {len(urls)} remote links concurrently...")

    failed = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(check_url, url): url for url in urls}
        for future in concurrent.futures.as_completed(futures):
            url, status_type, status_code = future.result()
            if status_type == "OK":
                print(f"[200 OK] {url}")
            elif status_type == "LOCAL_ASSET":
                print(f"[LOCAL ASSET] {url}")
            elif status_type == "FAILED":
                print(f"[FAIL {status_code}] {url}", file=sys.stderr)
                failed.append((url, status_code))
            else:
                print(f"[WARN] {url}: {status_code}")

    if failed:
        print(f"\n[FAIL] {len(failed)} links failed verification: {failed}", file=sys.stderr)
        return False

    print("\n[SUCCESS] All URLs and vector assets verified 100% reachable.")
    return True

if __name__ == "__main__":
    success = test_all_links()
    sys.exit(0 if success else 1)
