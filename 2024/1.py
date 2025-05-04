# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from pathlib import Path

part1 = 0
part2 = 0
left = []
right = []
input = Path("input", Path(__file__).name).with_suffix(".txt")
for line in input.read_text().splitlines():
    L, R = line.split()
    left.append(int(L))
    right.append(int(R))
left.sort()
right.sort()
for i, L in enumerate(left):
    R = right[i]
    part1 += abs(L - R)
    part2 += L * right.count(L)
print(part1)
print(part2)
