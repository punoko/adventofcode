# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from collections import defaultdict
from math import gcd
from pathlib import Path

part1 = set()
part2 = set()
input = Path("input", Path(__file__).name).with_suffix(".txt")
GRID = input.read_text().splitlines()
ANTENNAS = defaultdict(list)
for y, row in enumerate(GRID):
    for x, frequency in enumerate(row):
        if frequency != ".":
            ANTENNAS[frequency].append((x, y))
for antennas in ANTENNAS.values():
    while len(antennas) > 1:
        a_x, a_y = antennas.pop()
        for b_x, b_y in antennas:
            v_x = (a_x - b_x) // gcd(a_x - b_x, a_y - b_y)
            v_y = (a_y - b_y) // gcd(a_x - b_x, a_y - b_y)
            x, y = a_x, a_y
            while 0 <= x < len(GRID[0]) and 0 <= y < len(GRID):
                if x == 2 * a_x - b_x:
                    part1.add((x, y))
                part2.add((x, y))
                x += v_x
                y += v_y
            x, y = a_x, a_y
            while 0 <= x < len(GRID[0]) and 0 <= y < len(GRID):
                if x == 2 * b_x - a_x:
                    part1.add((x, y))
                part2.add((x, y))
                x -= v_x
                y -= v_y
print(len(part1))
print(len(part2))
