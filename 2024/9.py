# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from pathlib import Path


def checksum(blocks: list[str]) -> int:
    sum = 0
    for position, id in enumerate(blocks):
        if id != ".":
            sum += position * int(id)
    return sum


input = Path("input", Path(__file__).name).with_suffix(".txt")
disk = [int(length) for length in input.read_text().strip()]
blocks = []
for i, length in enumerate(disk):
    if i % 2 == 0:  # files
        blocks.extend([str(i // 2)] * length)
    else:  # free space
        blocks.extend(["."] * length)

part1 = blocks.copy()
i = len(part1)
k = 0
while i > 0:
    i -= 1
    if part1[i] == ".":
        continue
    try:
        k = part1.index(".", k, i)
    except ValueError:
        break
    part1[k] = part1[i]
    part1[i] = "."
print(checksum(part1))

part2 = blocks.copy()
i = len(part2)
while i > 0:
    j = i
    i -= 1
    if part2[i] == ".":
        continue
    while i > 0 and part2[i - 1] == part2[i]:
        i -= 1
    try:
        k = part2.index(".", 0, i)
    except ValueError:
        break
    length = j - i
    free = ["."] * length
    while k < i:
        if part2[k : k + length] == free:
            part2[k : k + length] = part2[i:j]
            part2[i:j] = free
            break
        try:
            k = part2.index(".", k + 1, i)
        except ValueError:
            break
print(checksum(part2))
