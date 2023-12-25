INPUT = open("input/9.txt").read().strip()
HISTORY = [[int(x) for x in line.split()] for line in INPUT.splitlines()]


def extrapolate(history: list[int]) -> tuple[int, int]:
    if all(value == 0 for value in history):
        return 0, 0
    else:
        difference = []
        for i in range(len(history) - 1):
            difference.append(history[i + 1] - history[i])
        before, after = extrapolate(difference)
        return history[0] - before, history[-1] + after


PART1 = []
PART2 = []
for history in HISTORY:
    before, after = extrapolate(history)
    PART1.append(after)
    PART2.append(before)
print(sum(PART1))
print(sum(PART2))
