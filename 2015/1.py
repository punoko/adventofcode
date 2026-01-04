import sys

input = sys.stdin.read()
part1 = 0
part2 = 0

for i, char in enumerate(input, start=1):
    if char == "(":
        part1 += 1
    elif char == ")":
        part1 -= 1
    if part1 < 0 and part2 == 0:
        part2 = i

print(part1)
print(part2)
