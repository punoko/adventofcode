# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

import re
import sys
from pathlib import Path

part1 = 0
part2 = 0

input = Path("input", Path(__file__).name).with_suffix(".txt")
input = Path(sys.argv[1]) if len(sys.argv) > 1 else input

machines = []
button_a: tuple[int, int] | None = None
button_b: tuple[int, int] | None = None
prize: tuple[int, int] | None = None


def parse_line(line: str) -> tuple[int, int]:
    x, y = line.split(":")[1].split(",")
    x = x.lstrip(" X+=")
    y = y.lstrip(" Y+=")
    return int(x), int(y)


def parse_block(block: str):
    m = [p for p in map(parse_line, block.strip().splitlines())]
    return m[0][0], m[0][1], m[1][0], m[1][1], m[2][0], m[2][1]


for block in input.read_text().split("\n\n"):
    ax, ay, bx, by, px, py = parse_block(block)
    for i in range(0, px // ax + 1):
        j = (px - ax * i) // bx
        if ax * i + bx * j == px and ay * i + by * j == py:
            part1 += i * 3 + j
            break

print(part1)
print(part2)
