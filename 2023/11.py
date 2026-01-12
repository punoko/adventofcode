import sys
from itertools import combinations


def distance(
    a: tuple[int, int],
    b: tuple[int, int],
    empty_rows: set[int],
    empty_cols: set[int],
    expansion: int,
) -> int:
    row_min = min(a[0], b[0])
    col_min = min(a[1], b[1])
    row_max = max(a[0], b[0])
    col_max = max(a[1], b[1])
    row_dist = row_max - row_min
    col_dist = col_max - col_min
    row_dist += expansion * len(empty_rows & set(range(row_min, row_max)))
    col_dist += expansion * len(empty_cols & set(range(col_min, col_max)))
    return row_dist + col_dist


universe = sys.stdin.read().splitlines()
R = len(universe)
C = len(universe[0])
galaxies = {(r, c) for r in range(R) for c in range(C) if universe[r][c] == "#"}
empty_rows = {r for r, row in enumerate(universe) if "#" not in row}
empty_cols = {c for c, col in enumerate(zip(*universe, strict=True)) if "#" not in col}

part1 = 0
part2 = 0
for a, b in combinations(galaxies, r=2):
    part1 += distance(a, b, empty_rows, empty_cols, expansion=1)
    part2 += distance(a, b, empty_rows, empty_cols, expansion=999999)
print(part1)
print(part2)
