import sys
from itertools import combinations

input = sys.stdin.read()
part1 = 0
part2 = 0

EGGNOG = 150
containers = [int(n) for n in input.splitlines()]
found = False
for r in range(4, len(containers)):
    for comb in combinations(containers, r=r):
        if sum(comb) == EGGNOG:
            part1 += 1
    if not found and part1:
        found = True
        part2 = part1

print(part1)
print(part2)
