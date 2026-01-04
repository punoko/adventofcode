import sys
from itertools import chain

input = sys.stdin.read()

grid1 = [[0 for _ in range(1000)] for _ in range(1000)]
grid2 = [[0 for _ in range(1000)] for _ in range(1000)]
for line in input.splitlines():
    *action, a, _, b = line.split()
    action = action[-1]
    ax, ay = map(int, a.split(","))
    bx, by = map(int, b.split(","))
    for y in range(ay, by + 1):
        for x in range(ax, bx + 1):
            if action == "on":
                grid1[y][x] = 1
                grid2[y][x] += 1
            elif action == "off":
                grid1[y][x] = 0
                grid2[y][x] -= 1 if grid2[y][x] else 0
            elif action == "toggle":
                grid1[y][x] ^= 1
                grid2[y][x] += 2
part1 = sum(light for light in chain.from_iterable(grid1))
part2 = sum(light for light in chain.from_iterable(grid2))

print(part1)
print(part2)
