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
    if operator == "+":
        part1 += sum(numbers)
    else:
        part1 += math.prod(numbers)


G = [line for line in input.split("\n") if line]
ROW = len(G)
COL = len(G[0])
operator = ""
numbers = []
for c in range(COL):
    if G[-1][c] != " ":
        operator = G[-1][c]
    string = [G[r][c] for r in range(ROW - 1)]
    string = "".join(string).strip()
    if string:
        numbers.append(int(string))
        if c < COL - 1:
            continue
    if operator == "+":
        part2 += sum(numbers)
    elif operator == "*":
        part2 += math.prod(numbers)
    numbers = []


print(part1)
print(part2)
