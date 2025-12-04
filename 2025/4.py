import sys


def get(map, r: int, c: int) -> str:
    if r < 0 or r >= ROW or c < 0 or c >= COL:
        return "!"
    return map[r][c]


def can_access_roll(map, row: int, col: int) -> bool:
    neigh = 0
    for dir in DIRECTIONS:
        r = row + dir[0]
        c = col + dir[1]
        if get(map, r, c) == "@":
            neigh += 1
    return neigh < MAX_ROLLS


input = sys.stdin.read()
part1 = 0
part2 = 0

MAP = tuple(tuple(r) for r in input.splitlines())
ROW = len(MAP)
COL = len(MAP[0])
DIRECTIONS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
MAX_ROLLS = 4
map = [list(row) for row in MAP]
while True:
    changed = False
    for r, line in enumerate(map):
        for c, char in enumerate(line):
            if char != "@":
                continue
            if can_access_roll(map, r, c):
                changed = True
                map[r][c] = "."
                part2 += 1
    if not changed:
        break
print(part1)
print(part2)
