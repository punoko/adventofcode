import sys

input = sys.stdin.read()
part1 = 0
part2 = 0

for line in input.splitlines():
    batteries = [int(x) for x in line]
    digit = max(batteries[:-1])
    index = batteries.index(digit) + 1
    part1 += digit * 10
    digit = max(batteries[index:])
    part1 += digit

print(part1)
print(part2)
