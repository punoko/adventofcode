import sys

input = sys.stdin.read()
part1 = 0
part2 = 0

for group in input.split("\n\n"):
    answers = group.splitlines()
    anyone = set(answers[0]).union(*answers[1:])
    part1 += len(anyone)
    everyone = set(answers[0]).intersection(*answers[1:])
    part2 += len(everyone)

print(part1)
print(part2)
