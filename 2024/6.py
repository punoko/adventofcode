# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from pathlib import Path


input = Path("input", Path(__file__).name).with_suffix(".txt")
MAP = tuple(input.read_text().splitlines())
Y_MAX = len(MAP)
X_MAX = len(MAP[0])
DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))

start_x = None
start_y = None
for y, line in enumerate(MAP):
    if "^" in line:
        start_y = y
        start_x = line.index("^")
        break
if start_x is None or start_y is None:
    raise ValueError("starting position not found")


SEEN_P1 = set()
part1 = 0
part2 = 0
for y, line in enumerate(MAP):
    for x, _ in enumerate(line):
        direction = 0
        pos_x = start_x
        pos_x = start_y
        SEEN_P1 = set()
        SEEN_P2 = set()
        while True:
            if (pos_x, pos_x, direction) in SEEN_P2:
                part2 += 1
                break
            SEEN_P1.add((pos_x, pos_x))
            SEEN_P2.add((pos_x, pos_x, direction))
            next_x = pos_x + DIRECTIONS[direction][0]
            next_y = pos_x + DIRECTIONS[direction][1]
            if not (0 <= next_x < X_MAX and 0 <= next_y < Y_MAX):
                # out of bounds
                break
            elif MAP[next_y][next_x] == "#" or (next_x, next_y) == (x, y):
                # turn right
                direction = (direction + 1) % len(DIRECTIONS)
            else:
                # move forward
                pos_x = next_x
                pos_x = next_y
        if MAP[y][x] == "#":
            part1 = len(SEEN_P1)
print(part1)
print(part2)
