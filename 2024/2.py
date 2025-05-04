# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from pathlib import Path


def is_safe(levels: list[int]) -> bool:
    diff = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
    if all(d > 0 and d < 4 for d in diff):
        return True
    elif all(d < 0 and d > -4 for d in diff):
        return True
    else:
        return False


part1 = 0
part2 = 0
input = Path("input", Path(__file__).name).with_suffix(".txt")
for line in input.read_text().splitlines():
    levels = [int(x) for x in line.split()]
    if is_safe(levels):
        part1 += 1
        part2 += 1
        continue
    for i, _ in enumerate(levels):
        dampened = levels.copy()
        del dampened[i]
        if is_safe(dampened):
            part2 += 1
            break
print(part1)
print(part2)
