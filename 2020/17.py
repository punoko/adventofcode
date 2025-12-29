import sys
from functools import cache
from itertools import chain, product

type Coordinates = tuple[int, ...]
type Grid = set[Coordinates]

CYCLES = 6
REMAIN_ACTIVE = (2, 3)
BECOME_ACTIVE = (3,)


@cache
def get_offsets(dimensions: int) -> list[Coordinates]:
    offsets = product((-1, 0, 1), repeat=dimensions)
    return [offset for offset in offsets if any(offset)]


def get_neighbors(cube: Coordinates) -> list[Coordinates]:
    return [
        tuple(c + o for c, o in zip(cube, offset, strict=True))
        for offset in get_offsets(dimensions=len(cube))
    ]


def count_active_neighbors(cube: Coordinates, grid: Grid) -> int:
    return sum(1 for neighbor in get_neighbors(cube) if neighbor in grid)


def should_be_active(cube: Coordinates, grid: Grid) -> bool:
    count = count_active_neighbors(cube, grid)
    return (cube in grid and count in REMAIN_ACTIVE) or (
        cube not in grid and count in BECOME_ACTIVE
    )


def run_cycle(grid: Grid) -> Grid:
    # first tried to do go through ranges from min and max of each dimension
    """
    dimensions = zip(*grid, strict=True)
    bounds = [range(min(d) - 1, max(d) + 2) for d in dimensions]
    neighborhood = product(*bounds)
    """
    # but only looking at the actual neighbors was 40% faster
    neighborhood = chain.from_iterable(get_neighbors(cube) for cube in grid)
    neighborhood = set(neighborhood).union(grid)
    return {cube for cube in neighborhood if should_be_active(cube, grid)}


def init_grid(input_text: str, dimensions: int) -> Grid:
    zeros = (0,) * (dimensions - 2)
    return {
        (x, y, *zeros)
        for x, line in enumerate(input_text.splitlines())
        for y, char in enumerate(line)
        if char == "#"
    }


input = sys.stdin.read()

part1 = init_grid(input, dimensions=3)
for _ in range(CYCLES):
    part1 = run_cycle(part1)
print(len(part1))

part2 = init_grid(input, dimensions=4)
for _ in range(CYCLES):
    part2 = run_cycle(part2)
print(len(part2))
