# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from pathlib import Path

part1 = 0
part2 = 0
input = Path("input", Path(__file__).name).with_suffix(".txt")
for line in input.read_text().splitlines():
    value, numbers = line.split(":")
    value = int(value)
    numbers = tuple(int(x) for x in numbers.split())
    for operators in range(2 ** (len(numbers) - 1)):
        result = numbers[0]
        for i, num in enumerate(numbers[1:]):
            if operators & 1 << i:
                result = result * num
            else:
                result = result + num
        if result == value:
            part1 += result
            break
print(part1)
print(part2)
