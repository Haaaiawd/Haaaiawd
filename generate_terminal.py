#!/usr/bin/env python3
"""Generate terminal GIF for the GitHub profile.

Shows a short "about me" session in a retro terminal: who I am,
the skills I work on, and my motto / vision. Produces ``output.gif``
in the working directory, ready to be merged with the pixel-profile
card by the GitHub Actions workflow.

Requires: ``pip install github-readme-terminal``
"""

import gifos

USERNAME = "Haaaiawd"

# 16:9 canvas matches the pixel-profile card so the two GIFs can be
# concatenated without letterboxing.
t = gifos.Terminal(width=640, height=360, xpad=14, ypad=14)
t.set_fps(15)

# whoami
t.gen_typing_text(
    f"\x1b[1;32m{USERNAME}@github\x1b[0m:~$ whoami", row_num=1, speed=2
)
t.gen_typing_text(f"\x1b[1;37m{USERNAME}\x1b[0m", row_num=2, speed=2)

# Skills
t.gen_typing_text(
    f"\x1b[1;32m{USERNAME}@github\x1b[0m:~$ cat skills.txt", row_num=4, speed=2
)
t.gen_typing_text("\x1b[1;36m- Agent Development\x1b[0m", row_num=5, speed=2)
t.gen_typing_text("\x1b[1;36m- AI Programming\x1b[0m", row_num=6, speed=2)
t.gen_typing_text("\x1b[1;36m- Prompt Engineering\x1b[0m", row_num=7, speed=2)

# Motto / vision
t.gen_typing_text(
    f"\x1b[1;32m{USERNAME}@github\x1b[0m:~$ cat motto.txt", row_num=9, speed=2
)
t.gen_typing_text(
    "\x1b[1;33mLet AI Illuminate Humanity's\x1b[0m", row_num=10, speed=2
)
t.gen_typing_text(
    "\x1b[1;33mRadiant Future of Goodness.\x1b[0m", row_num=11, speed=2
)

# Final blinking prompt
t.set_prompt(f"\x1b[1;32m{USERNAME}@github\x1b[0m:~$ ")
t.gen_prompt(row_num=13)

t.gen_gif()
print("Terminal GIF generated: output.gif")
