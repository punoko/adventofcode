import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readlines()
part1 = 0
part2 = 0

NUMBERS = tuple(int(n) for n in input)
preamble = 25
previous = deque(NUMBERS[:preamble], maxlen=preamble)
for num in NUMBERS[preamble:]:
    if any(a + b == num for a, b in combinations(previous, r=2)):
        previous.append(num)
        continue
    else:
        part1 = num
        break

for i in range(len(NUMBERS)):
    for j in range(i + 1, len(NUMBERS)):
        sequence = NUMBERS[i : j + 1]
        result = sum(sequence)
        if result == part1:
            part2 = min(sequence) + max(sequence)
            break
        elif result > part1:
            break
    if part2:
        break

print(part1)
print(part2)
