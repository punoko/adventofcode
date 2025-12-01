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

for line in input.read_text().splitlines():
    pass

print(part1)
print(part2)
