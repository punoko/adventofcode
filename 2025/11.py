import sys
from collections import deque

input = sys.stdin.read()
part1 = 0
part2 = 0

CONNECTIONS: dict[str, list[str]] = {}
for line in input.splitlines():
    key, values = line.split(":")
    CONNECTIONS[key] = values.strip().split()

paths = deque(CONNECTIONS["you"])
while paths:
    current = paths.popleft()
    if current == "out":
        part1 += 1
    else:
        paths.extend(CONNECTIONS[current])

print(part1)
print(part2)
