INPUT = open("input/6.txt").read().strip()
TIME, DISTANCE = [line.split(":")[1].split() for line in INPUT.splitlines()]


def func(time, distance):
    start = 0
    while start * (time - start) <= distance:
        start += 1
    end = time
    while end * (time - end) <= distance:
        end -= 1
    return len(range(start, end + 1))


part1 = 1
for i in range(len(TIME)):
    part1 *= func(int(TIME[i]), int(DISTANCE[i]))
part2 = func(int("".join(TIME)), int("".join(DISTANCE)))
print(part1)
print(part2)
