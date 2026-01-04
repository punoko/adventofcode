import re
import sys
from itertools import product

input = sys.stdin.read()
part1 = 0
part2 = 0

CALORIES = 500
TEASPOONS = 100
INGREDIENTS: list[tuple[int, int, int, int, int]] = []
for line in input.splitlines():
    name, _data = line.split(": ")
    data = re.findall(r"-?\d+", _data)
    cap, dur, fla, tex, cal = map(int, data)
    INGREDIENTS.append((cap, dur, fla, tex, cal))

_cap, _dur, _fla, _tex, _cal = zip(*INGREDIENTS, strict=True)
for recipe in product(range(TEASPOONS + 1), repeat=len(INGREDIENTS)):
    if sum(recipe) != TEASPOONS:
        continue
    cap = sum(i * q for i, q in zip(_cap, recipe, strict=True))
    dur = sum(i * q for i, q in zip(_dur, recipe, strict=True))
    fla = sum(i * q for i, q in zip(_fla, recipe, strict=True))
    tex = sum(i * q for i, q in zip(_tex, recipe, strict=True))
    cal = sum(i * q for i, q in zip(_cal, recipe, strict=True))
    score = max(cap, 0) * max(dur, 0) * max(fla, 0) * max(tex, 0)
    part1 = max(part1, score)
    if cal == CALORIES:
        part2 = max(part2, score)

print(part1)
print(part2)
