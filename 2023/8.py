from math import lcm

INPUT = open("input/8.txt").read().strip()
directions, m = INPUT.split("\n\n")
MAP = {}
for line in m.replace("=", "").splitlines():
    pos, left, right = [item.strip("(,)") for item in line.split()]
    MAP[pos] = {"L": left, "R": right}


def solve(positions: list[str], end: str):
    steps = []
    for pos in positions:
        step = 0
        while not pos.endswith(end):
            for next in directions:
                pos = MAP[pos][next]
                step += 1
                if pos.endswith(end):
                    break
        steps.append(step)
    return lcm(*steps)


part1 = ["AAA"]
print(solve(part1, "ZZZ"))

part2 = []
for key in MAP:
    if key.endswith("A"):
        part2.append(key)
print(solve(part2, "Z"))
