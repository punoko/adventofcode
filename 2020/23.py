import sys


def init(input_cups: tuple[int, ...], count: int) -> dict[int, int]:
    cups = list(range(1, count + 1))
    cups[0 : len(input_cups)] = input_cups
    return {cups[i - 1]: cups[i] for i in range(count)}


def apply_rules(current: int, clockwise: dict[int, int]) -> int:
    remove_1 = clockwise[current]
    remove_2 = clockwise[remove_1]
    remove_3 = clockwise[remove_2]

    destination = current - 1
    while destination in (remove_1, remove_2, remove_3) or destination < 1:
        destination -= 1
        if destination < 1:
            destination = max(clockwise)

    next = clockwise[remove_3]
    clockwise[current] = next
    clockwise[remove_3] = clockwise[destination]
    clockwise[destination] = remove_1
    return next


input = sys.stdin.read()
CUPS = tuple(int(n) for n in input.strip())

# part1
clockwise = init(CUPS, len(CUPS))
current = CUPS[0]
for _ in range(100):
    current = apply_rules(current, clockwise)

cup = 1
part1 = []
for _ in CUPS[1:]:
    cup = clockwise[cup]
    part1.append(str(cup))
print("".join(part1))

# part2
clockwise = init(CUPS, 1000000)
current = CUPS[0]
for _ in range(10000000):
    current = apply_rules(current, clockwise)

part2 = clockwise[1] * clockwise[clockwise[1]]
print(part2)
