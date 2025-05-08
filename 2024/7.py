# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from pathlib import Path

part1 = 0
part2 = 0
input = Path("input", Path(__file__).name).with_suffix(".txt")
for line in input.read_text().splitlines():
    numbers = [int(n) for n in line.replace(":", "").split()]
    value = numbers.pop(0)
    first = numbers.pop(0)
    found = False
    for seed in range(3 ** len(numbers)):
        result = first
        concat = False
        for i, num in enumerate(numbers):
            operator = (seed // (3**i)) % 3
            if operator == 0:
                result += num
            elif operator == 1:
                result *= num
            elif operator == 2:
                result = int(str(result) + str(num))
                concat = True
        if result == value:
            found = True
            if not concat:
                part1 += value
                break
    if found:
        part2 += value
print(part1)
print(part2)
