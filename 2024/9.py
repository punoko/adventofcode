# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from pathlib import Path

part1 = 0
part2 = 0
input = Path("input", Path(__file__).name).with_suffix(".txt")
# input = Path("input/test.txt")
map = iter(int(d) for d in input.read_text().strip())

id = 0
blocks = []
for length in map:
    blocks.extend([str(id)] * length)
    id += 1
    try:
        length = next(map)
        blocks.extend(["."] * length)
    except StopIteration:
        break
while "." in blocks:
    last = blocks.pop()
    if last == ".":
        continue
    blocks[blocks.index(".")] = last
for position, id in enumerate(blocks):
    part1 += position * int(id)
print(part1)
print(part2)
