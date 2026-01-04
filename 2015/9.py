import sys
from itertools import chain, pairwise, permutations

input = sys.stdin.read()

DISTANCES = {
    frozenset(locations.split(" to ")): int(distance)
    for line in input.splitlines()
    for locations, distance in [line.split(" = ")]
}
LOCATIONS = set(chain.from_iterable(DISTANCES))
ROUTES = {
    sum(DISTANCES[frozenset(pair)] for pair in pairwise(perm))
    for perm in permutations(LOCATIONS, len(LOCATIONS))
}

print(min(ROUTES))  # part1
print(max(ROUTES))  # part2
