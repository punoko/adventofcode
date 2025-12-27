import sys

input = sys.stdin.read().splitlines()
R = len(input)
C = len(input[0])


def count_neighbors(grid: list[list[str]], r: int, c: int, fist_seat: bool) -> int:
    count = 0
    for i, j in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        m = 1
        while True:
            rr = r + i * m
            cc = c + j * m
            if 0 <= rr < R and 0 <= cc < C:
                if grid[rr][cc] == "#":
                    count += 1
            else:
                break
            if not fist_seat or grid[rr][cc] != ".":
                break
            m += 1
    return count


def apply_rules(grid: list[list[str]], tolerance: int, fist_seat: bool) -> bool:
    changed = False
    new = [list(s) for s in grid]
    for r, row in enumerate(grid):
        for c, s in enumerate(row):
            if s == ".":
                continue
            n = count_neighbors(grid, r, c, fist_seat)
            if s == "L" and n == 0:
                new[r][c] = "#"
                changed = True
            elif s == "#" and n >= tolerance:
                new[r][c] = "L"
                changed = True
    grid[:] = new
    return changed


def count_occupied(grid: list[list[str]]) -> int:
    result = 0
    for row in grid:
        for char in row:
            if char == "#":
                result += 1
    return result


grid = [list(s) for s in input]
while apply_rules(grid, tolerance=4, fist_seat=False):
    pass
print(count_occupied(grid))  # part 1

grid = [list(s) for s in input]
while apply_rules(grid, tolerance=5, fist_seat=True):
    pass
print(count_occupied(grid))  # part 2
