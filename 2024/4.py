# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from pathlib import Path


def get(x, y) -> str:
    if y < 0 or y >= Y:
        return ""
    elif x < 0 or x >= X:
        return ""
    else:
        return LINES[y][x]


def walk(x, y, direction) -> bool:
    for c in "MAS":
        x += direction[0]
        y += direction[1]
        if not get(x, y) == c:
            return False
    return True


def cross(x, y) -> bool:
    corners = get(x - 1, y - 1)
    corners += get(x - 1, y + 1)
    corners += get(x + 1, y - 1)
    corners += get(x + 1, y + 1)
    if corners in ("MMSS", "MSMS", "SSMM", "SMSM"):
        return True
    else:
        return False


part1 = 0
part2 = 0
input = Path("input", Path(__file__).name).with_suffix(".txt")
LINES = input.read_text().splitlines()
Y = len(LINES)
X = len(LINES[0])
DIRECTIONS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
for y, line in enumerate(LINES):
    for x, char in enumerate(line):
        if char == "X":
            for direction in DIRECTIONS:
                if walk(x, y, direction):
                    part1 += 1
        elif char == "A":
            if cross(x, y):
                part2 += 1
print(part1)
print(part2)
