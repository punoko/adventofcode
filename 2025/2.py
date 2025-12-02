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


def check_range(a: str, b: str) -> set[int]:
    invalid = set()

    upper = int("9" * len(a)) + 1
    if upper in range(int(a), int(b) + 1):
        invalid |= check_range(str(upper), b)

    possible_length = [x for x in range(1, len(a) // 2 + 1) if len(a) % x == 0]
    for length in possible_length:
        for pattern in range(int(a[:length]), int("9" * length) + 1):
            num = int(str(pattern) * (len(a) // length))
            if num in range(int(a), int(b) + 1):
                invalid.add(num)
    return invalid

for r in input.read_text().split(","):
    a, b = r.strip().split("-")
    invalid = check_range(a, b)
    for n in invalid:
        part2 += n
        nstr = str(n)[: len(str(n)) // 2]
        if str(n) == f"{nstr}{nstr}":
            part1 += n


print(part1)
print(part2)
