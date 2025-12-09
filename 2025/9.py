import sys
from itertools import combinations

type Tile = tuple[int, int]


def area(a: Tile, b: Tile) -> int:
    return (abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1)


input = sys.stdin.read()

part2 = 0
red_tiles: list[Tile] = [
    (int(x), int(y))
    for line in input.splitlines()
    for x, y in [line.split(",")]
]
part1 = max(area(a, b) for a, b in combinations(red_tiles, 2))

print(part1)
print(part2)
