import sys
from collections import defaultdict

input = sys.stdin.read()
part1 = 0

# count timelines for each beam, start with 1
GRID = input.splitlines()
start = GRID.pop(0).index("S")
beams: dict[int, int] = defaultdict(int)
beams[start] = 1
while GRID:
    row = GRID.pop(0)
    for i, space in enumerate(row):
        if i in beams and space == "^":
            part1 += 1
            beams[i - 1] += beams[i]
            beams[i + 1] += beams[i]
            del beams[i]
part2 = sum(beams.values())

print(part1)
print(part2)
