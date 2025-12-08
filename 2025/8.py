import math
import sys
from itertools import combinations

input = sys.stdin.read()

type Box = tuple[int, int, int]
boxes: list[Box] = [
    (int(x), int(y), int(z))
    for line in input.splitlines()
    for x, y, z in [line.split(",")]
]
pairs = sorted(
    combinations(boxes, 2),
    key=lambda p: math.dist(p[0], p[1]),
)
circuits: list[set[Box]] = []
for i, (a, b) in enumerate(pairs, 1):
    new: list[set[Box]] = []
    connected = {a, b}
    for c in circuits:
        if a in c or b in c:
            connected.update(c)
        else:
            new.append(c)
    new.append(connected)
    circuits = new

    CONNECTIONS = 1000
    if i == CONNECTIONS:
        circuits.sort(key=len, reverse=True)
        # part1
        print(math.prod(len(c) for c in circuits[:3]))

    if len(circuits[0]) == len(boxes):
        # part2
        print(a[0] * b[0])
        break
