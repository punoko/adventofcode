import sys
from itertools import chain


def adjacent(x: int, y: int) -> list[tuple[int, int]]:
    return [(x + xx, y + yy) for xx, yy in DIRECTIONS.values()]


# the hexagonal grid as a normal 2d square grid
# except one diagonal is counted as adjacent
DIRECTIONS = {
    "w": (-1, 0),
    "e": (1, 0),
    "ne": (0, -1),
    "sw": (0, 1),
    "nw": (-1, -1),
    "se": (1, 1),
}
BECOME_BLACK = (2,)
REMAIN_BLACK = (1, 2)
BLACK = set()
input = sys.stdin.read()
for line in input.splitlines():
    characters = list(line)
    x = 0
    y = 0
    while characters:
        d = characters.pop(0)
        if d not in DIRECTIONS:
            d += characters.pop(0)
        x += DIRECTIONS[d][0]
        y += DIRECTIONS[d][1]
    # if (x,y) in set remove it, else add it
    BLACK.symmetric_difference_update({(x, y)})
print(len(BLACK))  # part1

for _ in range(100):
    tmp = set()
    tiles = chain.from_iterable(adjacent(*tile) for tile in BLACK)
    tiles = set(tiles).union(BLACK)
    for tile in tiles:
        count = sum(tile in BLACK for tile in adjacent(*tile))
        if (tile in BLACK and count in REMAIN_BLACK) or (
            tile not in BLACK and count in BECOME_BLACK
        ):
            tmp.add(tile)
    BLACK = tmp
print(len(BLACK))  # part2
