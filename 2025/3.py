import sys

input = sys.stdin.read()
part1 = 0
part2 = 0

for line in input.splitlines():
    bank = [int(x) for x in line]

    battery = max(bank[:-1])
    i = bank.index(battery) + 1
    part1 += battery * 10
    part1 += max(bank[i:])

    joltage = 0
    i = 0
    for j in range(-11, 1):
        joltage *= 10
        if j:
            slice = bank[i:j]
        else:
            slice = bank[i:]
        battery = max(slice)
        i += slice.index(battery) + 1
        joltage += battery
    part2 += joltage

print(part1)
print(part2)
