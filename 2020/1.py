import sys
from itertools import combinations

numbers = [int(n) for n in sys.stdin.read().splitlines()]

for a, b in combinations(numbers, 2):
    if a + b == 2020:
        part1 = a * b

for a, b, c in combinations(numbers, 3):
    if a + b + c == 2020:
        part2 = a * b * c

print(part1)
print(part2)
