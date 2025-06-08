# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from pathlib import Path

part1 = 0
part2 = 0
input = Path("input", Path(__file__).name).with_suffix(".txt")
# input = Path("input/test.txt")
stones = input.read_text().split()
for blink in range(25):
    tmp = []
    for stone in stones:
        if stone == "0":
            tmp.append("1")
        elif not len(stone) % 2:
            half = int(len(stone) / 2)
            tmp.append(str(int(stone[:half])))
            tmp.append(str(int(stone[half:])))
        else:
            tmp.append(str(int(stone) * 2024))
    stones = tmp
print(len(stones))
print(part2)
