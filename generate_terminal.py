#!/usr/bin/env python3
"""
Generate terminal GIF for GitHub profile
Requires: pip install github-readme-terminal
"""

import gifos
import os

# Configuration
USERNAME = "Haaaiawd"

# Create terminal
t = gifos.Terminal(width=320, height=200, xpad=5, ypad=5)
t.set_fps(15)

# Display user info
t.gen_text(text=f"{USERNAME}@github", row_num=1)
t.gen_text(text="", row_num=2)

# Fetch GitHub stats
github_token = os.environ.get('GITHUB_TOKEN')
if github_token:
    try:
        github_stats = gifos.utils.fetch_github_stats(user_name=USERNAME)
        t.gen_text(text=f"Repos: {github_stats.total_public_repos}", row_num=3)
        t.gen_text(text=f"Stars: {github_stats.total_stars}", row_num=4)
        t.gen_text(text=f"Followers: {github_stats.followers}", row_num=5)
    except Exception as e:
        print(f"Error fetching GitHub stats: {e}")
        t.gen_text(text="Repos: --", row_num=3)
        t.gen_text(text="Stars: --", row_num=4)
        t.gen_text(text="Followers: --", row_num=5)
else:
    t.gen_text(text="Repos: --", row_num=3)
    t.gen_text(text="Stars: --", row_num=4)
    t.gen_text(text="Followers: --", row_num=5)

# Generate GIF
t.gen_gif()

print("Terminal GIF generated: output.gif")
