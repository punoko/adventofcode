import sys
from itertools import chain, product

type Light = tuple[int, int]


def get_neighbors(light: Light) -> list[Light]:
    return [
        (c + cc, r + rr)
        for c, r in [light]
        for cc, rr in OFFSETS
        if (0 <= c + cc <= C and 0 <= r + rr <= R)
    ]


def count_neighbors_on(light: Light, grid: set[Light]) -> int:
    return sum(1 for l in get_neighbors(light) if l in grid)


def should_be_on(light: Light, grid: set[Light]) -> int:
    count = count_neighbors_on(light, grid)
    return (light in grid and count in REMAIN_ON) or (
        light not in grid and count in BECOME_ON
    )


def run_step(grid: set[Light]) -> set[Light]:
    neighborhood = chain.from_iterable([get_neighbors(l) for l in grid])
    neighborhood = set(neighborhood).union(grid)
    return {light for light in neighborhood if should_be_on(light, grid)}


input = sys.stdin.read()
STEPS = 100
REMAIN_ON = (2, 3)
BECOME_ON = (3,)
R = len(input.splitlines()) - 1
C = len(input.splitlines()[0]) - 1
OFFSETS = [offset for offset in product((-1, 0, 1), repeat=2) if any(offset)]
CORNERS = {(0, 0), (0, C), (R, 0), (R, C)}
GRID: set[Light] = {
    (r, c)
    for r, row in enumerate(input.splitlines())
    for c, char in enumerate(row)
    if char == "#"
}

grid = GRID.copy()
for _ in range(STEPS):
    grid = run_step(grid)
print(len(grid))  # part1

grid = GRID.copy()
grid.update(CORNERS)
for _ in range(STEPS):
    grid = run_step(grid)
    grid.update(CORNERS)
print(len(grid))  # part2
