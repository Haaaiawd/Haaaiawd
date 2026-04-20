#!/usr/bin/env python3
"""
Generate terminal GIF for GitHub profile
Requires: pip install github-readme-terminal
"""

import gifos
import os
import requests
from PIL import Image

# Configuration
USERNAME = "Haaaiawd"
AVATAR_URL = f"https://github.com/{USERNAME}.png"

# Download avatar
avatar_path = "avatar.png"
try:
    response = requests.get(AVATAR_URL)
    with open(avatar_path, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded avatar to {avatar_path}")
except Exception as e:
    print(f"Error downloading avatar: {e}")
    avatar_path = None

# Create terminal with pixel-style font
t = gifos.Terminal(width=400, height=300, xpad=10, ypad=10)
t.set_fps(15)

# Boot sequence with typing effect
t.gen_typing_text("Initializing system...", row_num=1, speed=2)
t.gen_typing_text("Loading user profile...", row_num=2, speed=2)

# Clear screen
for i in range(1, 3):
    t.delete_row(row_num=i)

# Display avatar if available
if avatar_path and os.path.exists(avatar_path):
    try:
        t.paste_image(avatar_path, row_num=1, col_num=1, size_multiplier=0.8)
    except Exception as e:
        print(f"Error pasting avatar: {e}")

# Display user info with typing effect
t.gen_typing_text(f"User: {USERNAME}", row_num=4, speed=2)

# Fetch GitHub stats
github_token = os.environ.get('GITHUB_TOKEN')
if github_token:
    try:
        github_stats = gifos.utils.fetch_github_stats(user_name=USERNAME)
        t.gen_typing_text(f"Repos: {github_stats.total_public_repos}", row_num=5, speed=2)
        t.gen_typing_text(f"Stars: {github_stats.total_stars}", row_num=6, speed=2)
        t.gen_typing_text(f"Followers: {github_stats.followers}", row_num=7, speed=2)
    except Exception as e:
        print(f"Error fetching GitHub stats: {e}")
        t.gen_typing_text("Repos: --", row_num=5, speed=2)
        t.gen_typing_text("Stars: --", row_num=6, speed=2)
        t.gen_typing_text("Followers: --", row_num=7, speed=2)
else:
    t.gen_typing_text("Repos: --", row_num=5, speed=2)
    t.gen_typing_text("Stars: --", row_num=6, speed=2)
    t.gen_typing_text("Followers: --", row_num=7, speed=2)

# Add skills
t.gen_typing_text("Skills: Agent Development, AI Programming", row_num=8, speed=2)
t.gen_typing_text("Prompt Engineering", row_num=9, speed=2, contin=True)

# Generate prompt
t.set_prompt(f"{USERNAME}@github ~> ")
t.gen_prompt(row_num=11)

# Generate GIF
t.gen_gif()

print("Terminal GIF generated: output.gif")

# Clean up
if avatar_path and os.path.exists(avatar_path):
    os.remove(avatar_path)
