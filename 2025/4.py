import sys


def is_roll(r: int, c: int) -> bool:
    return r >= 0 and r < ROW and c >= 0 and c < COL and GRID[r][c] == "@"


def can_access(row: int, col: int) -> bool:
    adj = 0
    for dir in DIRECTIONS:
        r = row + dir[0]
        c = col + dir[1]
        adj += 1 if is_roll(r, c) else 0
    return adj < MAX


input = sys.stdin.read()
part1 = 0
part2 = 0

DIRECTIONS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
GRID = [list(line) for line in input.splitlines()]
MAX = 4
ROW = len(GRID)
COL = len(GRID[0])

first = True
while True:
    changed = False
    tmp = [line.copy() for line in GRID]
    for r, row in enumerate(GRID):
        for c, char in enumerate(row):
            if char != "@":
                continue
            if can_access(r, c):
                changed = True
                tmp[r][c] = "x"
                if first:
                    part1 += 1
                part2 += 1
    first = False
    GRID = tmp
    if not changed:
        break

print(part1)
print(part2)
