import sys

input = sys.stdin.read()
part1 = 0
part2 = 0

G = input.splitlines()
beams = set()
beams.add(G.pop(0).index("S"))
while G:
    new = set()
    row = G.pop(0)
    for i, space in enumerate(row):
        if i not in beams:
            continue
        elif space == ".":
            # beam goes through
            pass
        elif space == "^":
            # beam is split
            beams.remove(i)
            beams.add(i - 1)
            beams.add(i + 1)
            part1 += 1

print(part1)
print(part2)
