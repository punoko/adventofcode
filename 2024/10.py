# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from pathlib import Path

part1 = 0
part2 = 0
input = Path("input", Path(__file__).name).with_suffix(".txt")
MAP = tuple(input.read_text().splitlines())
for r, row in enumerate(MAP):
    for c, char in enumerate(row):
        if char != "0":
            continue
        trails = [(r, c)]
        for height in range(1, 10):
            tmp = []
            while trails:
                x, y = trails.pop()
                for xx, yy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                    if 0 <= x + xx < len(MAP) and 0 <= y + yy < len(MAP[0]):
                        if MAP[x + xx][y + yy] == str(height):
                            tmp.append((x + xx, y + yy))
            trails = tmp
        part1 += len(set(trails))
        part2 += len(trails)
print(part1)
print(part2)
