import sys

input = sys.stdin.read()
part1 = 0
part2 = 0

for line in input.splitlines():
    dimensions = [int(n) for n in line.split("x")]
    l, w, h = sorted(dimensions)  # h is always the largest
    surface = 2 * l * w + 2 * w * h + 2 * h * l
    slack = l * w
    ribbon = 2 * l + 2 * w
    volume = l * w * h
    part1 += surface + slack
    part2 += volume + ribbon

print(part1)
print(part2)
