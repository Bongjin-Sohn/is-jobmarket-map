#!/usr/bin/env python3
"""Wrap the self-contained artifact.html fragment into a full standalone
HTML document for GitHub Pages (adds charset, mobile viewport, noindex).

Source is the same artifact.html produced by the weekly update routine.
Run this after update_jobs.py, then `git commit && git push` to publish.
"""
import pathlib

SRC = pathlib.Path(
    "/Users/andrewsohn/Library/CloudStorage/Dropbox/Temp Dock/"
    "1. Doctoral Dissertation/Job market placement/"
    "R1_job_market_map/pipeline/artifact.html"
)
OUT = pathlib.Path(__file__).with_name("index.html")

HEAD = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow, noarchive">
<meta name="googlebot" content="noindex, nofollow">
<meta name="theme-color" content="#0d1117">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<title>IS Job Market Map</title>
</head>
<body>
"""

FOOT = "\n</body>\n</html>\n"


def main() -> None:
    body = SRC.read_text(encoding="utf-8")
    OUT.write_text(HEAD + body + FOOT, encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes) from {SRC.name}")


if __name__ == "__main__":
    main()
