#!/usr/bin/env python3
"""Generate terminal GIF for the GitHub profile.

Shows a short "about me" session in a retro terminal: who I am,
the skills I work on, and my motto / vision. Produces ``output.gif``
in the working directory, ready to be merged with the pixel-profile
card by the GitHub Actions workflow.

Commands are typed out character-by-character (fast), while their
"output" is rendered as a single block, the way a real shell prints
command output. Requires: ``pip install github-readme-terminal``.
"""

import gifos

USERNAME = "Haaaiawd"
PROMPT = f"\x1b[1;32m{USERNAME}@github\x1b[0m:~$ "

# 16:9 canvas matches the pixel-profile card so the two GIFs can be
# concatenated without letterboxing.
t = gifos.Terminal(width=640, height=360, xpad=14, ypad=14)
t.set_fps(15)

# speed=2 = medium (matches the original pacing);
# output lines use gen_text for instant, shell-style printing.
TYPING_SPEED = 2


def prompt_line(row: int, command: str) -> None:
    """Render a typed prompt + command on a single line."""
    t.gen_text(PROMPT, row_num=row)
    t.gen_typing_text(command, row_num=row, col_num=len(f"{USERNAME}@github:~$ ") + 1,
                      contin=True, speed=TYPING_SPEED)


# --- whoami ------------------------------------------------------------
prompt_line(1, "whoami")
t.gen_text(text=f"\x1b[1;37m{USERNAME}\x1b[0m", row_num=2)

# --- skills ------------------------------------------------------------
prompt_line(4, "cat skills.txt")
t.gen_text(text="\x1b[1;36m- Agent Development\x1b[0m", row_num=5)
t.gen_text(text="\x1b[1;36m- AI Programming\x1b[0m", row_num=6)
t.gen_text(text="\x1b[1;36m- Prompt Engineering\x1b[0m", row_num=7)

# --- motto -------------------------------------------------------------
prompt_line(9, "cat motto.txt")
t.gen_text(text="\x1b[1;33mLet AI Illuminate Humanity's\x1b[0m", row_num=10)
t.gen_text(text="\x1b[1;33mRadiant Future of Goodness.\x1b[0m", row_num=11)

# --- final blinking prompt --------------------------------------------
t.set_prompt(PROMPT)
t.gen_prompt(row_num=13)

t.gen_gif()
print("Terminal GIF generated: output.gif")
