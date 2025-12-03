import sys


def maximum_joltage(bank: list[int], count: int) -> int:
    joltage = 0
    i = 0
    for j in range(1 - count, 1):
        slice = bank[i:j] if j < 0 else bank[i:]
        battery = max(slice)
        joltage = 10 * joltage + battery
        i += slice.index(battery) + 1
    return joltage


input = sys.stdin.read()
part1 = 0
part2 = 0

for line in input.splitlines():
    bank = [int(n) for n in line]
    part1 += maximum_joltage(bank, 2)
    part2 += maximum_joltage(bank, 12)

print(part1)
print(part2)
