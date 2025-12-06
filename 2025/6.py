import math
import sys

input = sys.stdin.read()
part1 = 0
part2 = 0


GRID = [line.split() for line in input.splitlines() if line]
ROW = len(GRID)
COL = len(GRID[0])

for c in range(COL):
    operator = GRID[-1][c]
    numbers = [int(GRID[x][c]) for x in range(ROW - 1)]
    print(operator, numbers)
    if operator == "+":
        part1 += sum(numbers)
    else:
        part1 += math.prod(numbers)

print(part1)
print(part2)
