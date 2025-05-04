# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from pathlib import Path
import re

part1 = 0
part2 = 0
input = Path("input", Path(__file__).name).with_suffix(".txt")
pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
do = True
for match in re.finditer(pattern, input.read_text(), flags=re.MULTILINE):
    print(match.group())
    if match.group() == "do()":
        do = True
    elif match.group() == "don't()":
        do = False
    else:
        X = int(match.group(1))
        Y = int(match.group(2))
        part1 += X * Y
        if do:
            part2 += X * Y
print(part1)
print(part2)
