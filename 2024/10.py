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
        paths = []
        for height in range(10):
            paths.append(set())
            if height == 0:
                paths[height].add((r, c))
                continue
            for x, y in paths[height - 1]:
                for xx, yy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                    if 0 <= x + xx < len(MAP) and 0 <= y + yy < len(MAP[0]):
                        if MAP[x + xx][y + yy] == str(height):
                            paths[height].add((x + xx, y + yy))
        part1 += len(paths[9])
print(part1)
print(part2)
