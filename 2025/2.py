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


def check_range(a, b) -> set[int] | None:
    invalid = set()
    if len(a) % 2 == 0:
        start = a
    else:
        start = "1" + "0" * len(a)
    if int(start) > int(b):
        return
    elif len(b) % 2 == 0:
        end = b
    else:
        end = "9" * (len(b) - 1)
    if len(start) != len(end):
        raise ValueError("require split range: %s-%s", a, b)
    size = len(start) // 2
    h_start = int(start[:size])
    h_end = int(end[:size])
    for half in range(h_start, h_end + 1):
        test = int(f"{half}{half}")
        if test in range(int(start), int(end) + 1):
            invalid.add(test)
    return invalid


for r in input.read_text().split(","):
    a, b = r.strip().split("-")
    invalid = check_range(a, b)
    if not invalid:
        continue
    for n in invalid:
        part1 += n


print(part1)
print(part2)
