#!/usr/bin/env python3
"""
Generate terminal GIF for GitHub profile
Requires: pip install github-readme-terminal
"""

import gifos
import os

# Configuration
USERNAME = "Haaaiawd"
OUTPUT_FILE = "terminal.gif"

# Create terminal with pixel-style font
t = gifos.Terminal(width=320, height=240, xpad=5, ypad=5)

# Add boot sequence
t.gen_text(text="Booting system...", row_num=1)
t.gen_text(text="Loading kernel...", row_num=2)
t.gen_text(text="Starting services...", row_num=3)

# Clear screen after boot
for i in range(1, 4):
    t.delete_row(row_num=i)

# Add header - ASCII style without emoji
t.gen_text(text=f"+-- {USERNAME}@github --+", row_num=1, contin=True)
t.gen_text(text="|", row_num=2, contin=True)

# Fetch GitHub stats (requires GITHUB_TOKEN env var)
github_token = os.environ.get('GITHUB_TOKEN')
if github_token:
    try:
        github_stats = gifos.utils.fetch_github_stats(user_name=USERNAME)

        # Display stats - ASCII style
        t.gen_text(text=f"| [REPOS] {github_stats.total_public_repos}", row_num=3, contin=True)
        t.gen_text(text=f"| [STARS] {github_stats.total_stars}", row_num=4, contin=True)
        t.gen_text(text=f"| [FOLLOWERS] {github_stats.followers}", row_num=5, contin=True)
        t.gen_text(text=f"| [FOLLOWING] {github_stats.following}", row_num=6, contin=True)
    except Exception as e:
        print(f"Error fetching GitHub stats: {e}")
        t.gen_text(text="| [REPOS] Error", row_num=3, contin=True)
        t.gen_text(text="| [STARS] Error", row_num=4, contin=True)
        t.gen_text(text="| [FOLLOWERS] Error", row_num=5, contin=True)
        t.gen_text(text="| [FOLLOWING] Error", row_num=6, contin=True)
else:
    # Use demo data for preview
    print("No GITHUB_TOKEN found, using demo data for preview")
    t.gen_text(text="| [REPOS] 42", row_num=3, contin=True)
    t.gen_text(text="| [STARS] 1337", row_num=4, contin=True)
    t.gen_text(text="| [FOLLOWERS] 256", row_num=5, contin=True)
    t.gen_text(text="| [FOLLOWING] 128", row_num=6, contin=True)

# Add footer
t.gen_text(text="|", row_num=7, contin=True)
t.gen_text(text="+--------------------+", row_num=8, contin=True)

# Generate GIF
t.gen_gif()

print(f"Terminal GIF generated: {OUTPUT_FILE}")
