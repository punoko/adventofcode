# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from pathlib import Path


def solve(x: int, y: int) -> tuple[int, int]:
    if (x, y) in SEEN:
        return 0, 0
    SEEN.add((x, y))
    area = 1
    perim = 0
    for xx, yy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        if 0 <= x + xx < len(MAP) and 0 <= y + yy < len(MAP[0]):
            if MAP[x + xx][y + yy] == MAP[x][y]:
                a, p = solve(x + xx, y + yy)
                area += a
                perim += p
            else:
                perim += 1
        else:
            perim += 1
    return area, perim


part1 = 0
part2 = 0
input = Path("input", Path(__file__).name).with_suffix(".txt")
MAP = tuple(input.read_text().splitlines())
SEEN = set()
for x, line in enumerate(MAP):
    for y, plant in enumerate(line):
        if (x, y) not in SEEN:
            area, perim = solve(x, y)
            part1 += area * perim
print(part1)
print(part2)
