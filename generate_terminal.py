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

# Create terminal
t = gifos.Terminal(width=320, height=240, xpad=5, ypad=5)

# Add boot sequence
t.gen_text(text="Booting system...", row_num=1)
t.gen_text(text="Loading kernel...", row_num=2)
t.gen_text(text="Starting services...", row_num=3)

# Clear screen after boot
for i in range(1, 4):
    t.delete_row(row_num=i)

# Add header
t.gen_text(text=f"╭─ {USERNAME}@github ─╮", row_num=1, contin=True)
t.gen_text(text="│", row_num=2, contin=True)

# Fetch GitHub stats (requires GITHUB_TOKEN env var)
try:
    github_stats = gifos.utils.fetch_github_stats(user_name=USERNAME)
    
    # Display stats
    t.gen_text(text=f"│ 📦 Repos: {github_stats.total_public_repos}", row_num=3, contin=True)
    t.gen_text(text=f"│ ⭐ Stars: {github_stats.total_stars}", row_num=4, contin=True)
    t.gen_text(text=f"│ 🔄 Followers: {github_stats.followers}", row_num=5, contin=True)
    t.gen_text(text=f"│ 📝 Following: {github_stats.following}", row_num=6, contin=True)
except Exception as e:
    print(f"Error fetching GitHub stats: {e}")
    t.gen_text(text="│ 📦 Repos: Loading...", row_num=3, contin=True)
    t.gen_text(text="│ ⭐ Stars: Loading...", row_num=4, contin=True)
    t.gen_text(text="│ 🔄 Followers: Loading...", row_num=5, contin=True)
    t.gen_text(text="│ 📝 Following: Loading...", row_num=6, contin=True)

# Add footer
t.gen_text(text="│", row_num=7, contin=True)
t.gen_text(text=f"╰─────────────────────╯", row_num=8, contin=True)

# Generate GIF
t.gen_gif()

print(f"Terminal GIF generated: {OUTPUT_FILE}")
