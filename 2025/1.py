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

DIAL = 50

for line in input.read_text().splitlines():
    if line.startswith("L"):
        DIAL -= int(line[1:])
    elif line.startswith("R"):
        DIAL += int(line[1:])
    else:
        raise ValueError("bad line %s", line)
    DIAL = DIAL % 100
    if DIAL == 0:
        part1 += 1

print(part1)
print(part2)
