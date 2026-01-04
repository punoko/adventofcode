import sys
from collections import defaultdict
from itertools import pairwise, permutations

input = sys.stdin.read()
part1 = 0
part2 = 0

HAPPINESS = defaultdict(dict)
for line in input.splitlines():
    words = line.split()
    value = int(words[3])
    value *= 1 if "gain" in words else -1
    guest1 = words[0]
    guest2 = words[-1].rstrip(".")
    HAPPINESS[guest1][guest2] = value

names = list(HAPPINESS)
for perm in permutations(names[1:], len(names) - 1):
    table = [names[0], *perm, names[0]]
    scores = []
    for a, b in pairwise(table):
        value = HAPPINESS[a][b] + HAPPINESS[b][a]
        scores.append(value)
    part1 = max(sum(scores), part1)
    # optimally inserting yourself between two guests
    # is the same as removing the weakest score
    part2 = max(sum(sorted(scores)[1:]), part2)

print(part1)
print(part2)
