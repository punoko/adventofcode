import sys

input = sys.stdin.read()
part1 = 0
part2 = 0

for line in input.splitlines():
    password: str
    policy, char, password = line.split()
    a, b = (int(n) for n in policy.split("-"))
    char = char[:1]
    if a <= password.count(char) <= b:
        part1 += 1
    if (password[a - 1] == char) ^ (password[b - 1] == char):
        part2 += 1

print(part1)
print(part2)
