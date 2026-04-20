#!/usr/bin/env python3
"""
Generate terminal GIF for GitHub profile
Requires: pip install github-readme-terminal
"""

import gifos

# Configuration
USERNAME = "Haaaiawd"

# Create terminal with pixel-style font
t = gifos.Terminal(width=320, height=240, xpad=5, ypad=5)

# Add header - ASCII style
t.gen_text(text=f"+-- {USERNAME}@github --+", row_num=1, contin=True)
t.gen_text(text="|", row_num=2, contin=True)
t.gen_text(text="| Agent Development", row_num=3, contin=True)
t.gen_text(text="| AI Programming", row_num=4, contin=True)
t.gen_text(text="| Prompt Engineering", row_num=5, contin=True)

# Add footer
t.gen_text(text="|", row_num=6, contin=True)
t.gen_text(text="+--------------------+", row_num=7, contin=True)

# Generate GIF (uses default output.gif)
t.gen_gif()

print("Terminal GIF generated: output.gif")
