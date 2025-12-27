import sys
from functools import cache
from itertools import pairwise

adapters = [int(n) for n in sys.stdin.readlines()]
adapters = [0, *sorted(adapters), max(adapters) + 3]
differences = [b - a for a, b in pairwise(adapters)]


@cache
def arrangements_from(i: int) -> int:
    if i == len(adapters) - 1:
        return 1
    result = 0
    for j in range(i + 1, min(i + 4, len(adapters))):
        if adapters[j] - adapters[i] <= 3:
            result += arrangements_from(j)
    return result


part1 = differences.count(1) * differences.count(3)
part2 = arrangements_from(0)
print(part1)
print(part2)
