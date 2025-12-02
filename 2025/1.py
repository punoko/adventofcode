import sys

input = sys.stdin.read()
part1 = 0
part2 = 0

dial = 50
for line in input.splitlines():
    if line[0] == "L":
        step = -1
    else:
        step = +1
    distance = int(line[1:])
    for _ in range(distance):
        dial = (dial + step) % 100
        if dial == 0:
            part2 += 1
    if dial == 0:
        part1 += 1

print(part1)
print(part2)
