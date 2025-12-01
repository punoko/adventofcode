# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

import sys
from pathlib import Path

part1 = 0
part2 = 0

input = Path("input", Path(__file__).name).with_suffix(".txt")
input = Path(sys.argv[1]) if len(sys.argv) > 1 else input

start = 50

for i, line in enumerate(input.read_text().splitlines()):
    if line.startswith("L"):
        move = int(line[1:])
        step = -1
    elif line.startswith("R"):
        move = int(line[1:])
        step = +1
    else:
        raise ValueError("bad line %s", line)
    end = start + move * step
    for i in range(start + step, end + step, step):
        if i % 100 == 0:
            part2 += 1
    start = end % 100
    if start == 0:
        part1 += 1

print(part1)
print(part2)
