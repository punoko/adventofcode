import sys

input = sys.stdin.read()
part1 = 0

beams = [0] * input.index("\n")
beams[input.index("S")] = 1
for line in input.splitlines()[1:]:
    for i, c in enumerate(line):
        if c == "^" and beams[i]:
            part1 += 1
            beams[i - 1] += beams[i]
            beams[i + 1] += beams[i]
            beams[i] = 0
part2 = sum(beams)

print(part1)
print(part2)
