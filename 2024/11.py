# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from pathlib import Path

def solve(stone: int, depth: int) -> int:
    if (stone, depth) in SAVED:
        return SAVED[(stone, depth)]
    if depth == 0:
        return 1
    if stone == 0:
        result = solve(1, depth - 1)
    elif len(str(stone)) % 2 == 0:
        string = str(stone)
        half = len(string) // 2
        result = solve(int(string[:half]), depth - 1)
        result += solve(int(string[half:]), depth - 1)
    else:
        result = solve(stone * 2024, depth - 1)
    SAVED[(stone, depth)] = result
    return result


part1 = 0
part2 = 0
input = Path("input", Path(__file__).name).with_suffix(".txt")
SAVED = dict()
for stone in input.read_text().split():
    part1 += solve(int(stone), 25)
    part2 += solve(int(stone), 75)
print(part1)
print(part2)
