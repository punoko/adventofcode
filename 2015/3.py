import sys
from collections import defaultdict

DIRECTIONS = {
    ">": (1, 0),
    "<": (-1, 0),
    "v": (0, 1),
    "^": (0, -1),
}
input = sys.stdin.read()
part1 = defaultdict(int)
part2 = defaultdict(int)

part1[(0, 0)] = 1
part2[(0, 0)] = 1
x, y = 0, 0
x_robo, y_robo = 0, 0
x_santa, y_santa = 0, 0
for i, char in enumerate(input.strip()):
    xx, yy = DIRECTIONS[char]
    x += xx
    y += yy
    part1[x, y] += 1
    if i % 2:
        x_santa += xx
        y_santa += yy
        part2[x_santa, y_santa] += 1
    else:
        x_robo += xx
        y_robo += yy
        part2[x_robo, y_robo] += 1

print(len(part1))
print(len(part2))
