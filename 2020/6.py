import sys
from itertools import chain

input = sys.stdin.read()
part1 = 0
part2 = 0

for group in input.split("\n\n"):
    answers = group.splitlines()
    anyone = chain.from_iterable(group.splitlines())
    part1 += len(set(anyone))

    everyone = set(answers[0])
    for other in answers[1:]:
        everyone &= set(other)
    part2 += len(set(everyone))

print(part1)
print(part2)
