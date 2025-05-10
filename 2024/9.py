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

part2 = blocks.copy()
i = len(part2)
while True:
    j = i
    i -= 1
    if part2[i] == ".":
        continue
    while part2[i - 1] == part2[i]:
        i -= 1
    try:  # look for first free block left of i
        k = part2.index(".", 0, i)
    except ValueError:
        break
    length = j - i
    free = ["."] * length
    while True:
        if part2[k : k + length] != free:
            try:
                k = part2.index(".", k + 1, j)
                continue
            except ValueError:
                break
        part2[k : k + length] = part2[i:j]
        part2[i:j] = free
        break
print(checksum(part2))
