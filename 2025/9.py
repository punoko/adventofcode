import sys
from itertools import combinations, pairwise


def area(a: tuple[int, int], b: tuple[int, int]) -> int:
    return (abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1)


def inside_polygon(
    a: tuple[int, int],
    b: tuple[int, int],
    red_tiles: list[tuple[int, int]],
) -> bool:
    ax, ay = a
    bx, by = b
    minx = min(ax, bx)
    maxx = max(ax, bx)
    miny = min(ay, by)
    maxy = max(ay, by)

    # check that no segment goes through the sides of our rectangle
    for (ix, iy), (jx, jy) in pairwise(red_tiles):
        if (
            ix == jx  # vertical segment
            and minx < ix < maxx
            and (
                miny < iy < maxy
                or miny < jy < maxy
                or (iy <= miny and jy >= maxy)
                or (jy <= miny and iy >= maxy)
            )
        ) or (
            iy == jy  # horizontal segment
            and miny < iy < maxy
            and (
                minx < ix < maxx
                or minx < jx < maxx
                or (ix <= minx and jx >= maxx)
                or (jx <= minx and ix >= maxx)
            )
        ):
            return False

    # check that we are inside red/green tiles
    green_corner_1 = False
    green_corner_2 = False
    for x, y in red_tiles:
        if (ax <= bx and ay <= by) or (ax >= bx and ay >= by):
            if x <= minx and y >= maxy:
                green_corner_1 = True
            elif x >= maxx and y <= miny:
                green_corner_2 = True
        elif (ax <= bx and ay >= by) or (ax >= bx and ay <= by):
            if x <= minx and y <= miny:
                green_corner_1 = True
            elif x >= maxx and y >= maxy:
                green_corner_2 = True

    return green_corner_1 and green_corner_2


input = sys.stdin.read()

red_tiles: list[tuple[int, int]] = [
    (int(x), int(y))
    for line in input.splitlines()
    for x, y in [line.split(",")]
]
part1 = max(area(a, b) for a, b in combinations(red_tiles, 2))
part2 = max(
    area(a, b)
    for a, b in combinations(red_tiles, 2)
    if inside_polygon(a, b, red_tiles)
)

print(part1)
print(part2)
