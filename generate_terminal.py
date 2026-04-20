#!/usr/bin/env python3
"""
Generate terminal GIF for GitHub profile - Self Introduction
Requires: pip install github-readme-terminal
"""

import gifos

# Configuration
USERNAME = "Haaaiawd"

# Create terminal with 16:9 aspect ratio
t = gifos.Terminal(width=480, height=270, xpad=10, ypad=10)
t.set_fps(15)

# Display self introduction
t.gen_text(text=f"\x1b[1;32m{USERNAME}@github\x1b[0m", row_num=1)
t.gen_text(text="", row_num=2)
t.gen_text(text="\x1b[1;36mWhat I Do:\x1b[0m", row_num=3)
t.gen_text(text="  Agent Development", row_num=4)
t.gen_text(text="  AI Programming", row_num=5)
t.gen_text(text="  Prompt Engineering", row_num=6)
t.gen_text(text="", row_num=7)
t.gen_text(text="\x1b[1;33mVision:\x1b[0m", row_num=8)
t.gen_text(text="\x1b[1;37mLet AI Illuminate Humanity's Radiant Future of Goodness\x1b[0m", row_num=9)

# Generate GIF
t.gen_gif()

print("Terminal GIF generated: output.gif")
