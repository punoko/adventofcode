import sys
from collections import Counter
from itertools import pairwise

input = sys.stdin.read()
part1 = 0
part2 = 0

VOWELS = "aeiou"
MIN_VOWELS = 3
for string in input.splitlines():
    pairs = list(pairwise(string))
    counter = Counter(string)
    if (
        sum(counter[c] for c in VOWELS) >= MIN_VOWELS
        and any(p[0] == p[1] for p in pairs)
        and not any(sub in string for sub in ("ab", "cd", "pq", "xy"))
    ):
        part1 += 1

    triplets = [string[i : i + 3] for i in range(len(string) - 2)]
    if not any(t[0] == t[2] for t in triplets):
        continue
    doubles = ["".join(k) for k, v in Counter(pairs).items() if v > 1]
    for d in doubles:
        first = string.index(d)
        second = string.index(d, first + 1)
        if second - first > 1:
            part2 += 1
            break

print(part1)
print(part2)
