import math
import sys

input = sys.stdin.read()
part1 = 0
part2 = 0

GRID = [line for line in input.split("\n") if line]
OPERATORS = GRID.pop()
R = len(GRID)
C = len(GRID[0])

operator = ""
part1_numbers = []
part2_numbers = []
for c in range(C):
    if OPERATORS[c] != " ":
        operator = OPERATORS[c]
        horizontal = [GRID[r][c:].split()[0] for r in range(R)]
        part1_numbers = [int(n) for n in horizontal]

    vertical = [GRID[r][c] for r in range(R)]
    vertical = "".join(vertical).strip()
    if vertical:
        part2_numbers.append(int(vertical))
        if c < C - 1:
            continue

    if operator == "+":
        part1 += sum(part1_numbers)
        part2 += sum(part2_numbers)
    elif operator == "*":
        part1 += math.prod(part1_numbers)
        part2 += math.prod(part2_numbers)
    part2_numbers = []

print(part1)
print(part2)
