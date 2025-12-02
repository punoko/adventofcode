import sys

part1 = 0
part2 = 0

input = sys.stdin.read()

start = 50
for i, line in enumerate(input.splitlines()):
    if line.startswith("L"):
        move = int(line[1:])
        step = -1
    elif line.startswith("R"):
        move = int(line[1:])
        step = +1
    else:
        raise ValueError("bad line %s", line)
    end = start + move * step
    for i in range(start + step, end + step, step):
        if i % 100 == 0:
            part2 += 1
    start = end % 100
    if start == 0:
        part1 += 1

print(part1)
print(part2)
