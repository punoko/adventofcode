import sys


def get(r: int, c: int) -> str:
    if r < 0 or r >= ROW or c < 0 or c >= COL:
        return "!"
    return MAP[r][c]


def can_access_roll(row: int, col: int) -> bool:
    print("checking", row, col)
    neigh = 0
    for dir in DIRECTIONS:
        r = row + dir[0]
        c = col + dir[1]
        bla = get(r, c)
        print(bla, r, c)
        if bla == "@":
            neigh += 1
    print("total=", neigh)
    return neigh < MAX_ROLLS


input = sys.stdin.read()
part1 = 0
part2 = 0

MAP = tuple(input.splitlines())
ROW = len(MAP)
COL = len(MAP[0])
DIRECTIONS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
MAX_ROLLS = 4
for r, line in enumerate(MAP):
    for c, char in enumerate(line):
        if char != "@":
            print("char", char, r, c, "skipping")
            continue
        print("char", char, r, c, "OK")
        if can_access_roll(r, c):
            part1 += 1
print(part1)
print(part2)
