# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from pathlib import Path
from collections import defaultdict

input = Path("input", Path(__file__).name).with_suffix(".txt")
GRID = input.read_text().splitlines()
antennas = defaultdict(list)
for y, row in enumerate(GRID):
    for x, frequency in enumerate(row):
        if frequency != ".":
            antennas[frequency].append((x, y))
antinodes = set()
for frequency in antennas:
    tmp = antennas[frequency]
    while len(tmp) > 1:
        ax, ay = tmp.pop()
        for bx, by in tmp:
            for x, y in [
                (2 * ax - bx, 2 * ay - by),
                (2 * bx - ax, 2 * by - ay),
            ]:
                if 0 <= x < len(GRID[0]) and 0 <= y < len(GRID):
                    antinodes.add((x, y))
part1 = len(antinodes)
part2 = 0
print(part1)
print(part2)
