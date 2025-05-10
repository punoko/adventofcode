# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from pathlib import Path


def checksum(blocks: list[str]) -> int:
    sum = 0
    for pos, id in enumerate(blocks):
        if id != ".":
            sum += pos * int(id)
    return sum


input = Path("input", Path(__file__).name).with_suffix(".txt")
disk = [int(length) for length in input.read_text().strip()]
blocks = []
for i, length in enumerate(disk):
    if i % 2 == 0:  # file
        blocks.extend([str(i // 2)] * length)
    else:  # free space
        blocks.extend(["."] * length)

part1 = blocks.copy()
i = len(part1)
try:
    j = part1.index(".")
except ValueError:
    j = i
while i > j:
    i -= 1
    if part1[i] == ".":
        continue
    part1[j] = part1[i]
    part1[i] = "."
    try:
        j = part1.index(".", j + 1, i)
    except ValueError:
        break
print(checksum(part1))
