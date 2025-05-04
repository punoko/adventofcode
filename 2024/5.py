# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from pathlib import Path

def middle_page(pages: list[int]) -> int:
    return pages[int((len(pages) - 1) / 2)]


def correctly_ordered(pages: list[int]) -> bool:
    for X, Y in RULES:
        try:
            x = pages.index(X)
            y = pages.index(Y)
        except ValueError:
            continue
        if x > y:
            return False
    return True


def apply_rules(pages: list[int]) -> None:
    for X, Y in RULES:
        try:
            x = pages.index(X)
            y = pages.index(Y)
        except ValueError:
            continue
        if x > y:
            pages.insert(y, pages.pop(x))


part1 = 0
part2 = 0
input = Path("input", Path(__file__).name).with_suffix(".txt")
RULES = []
for line in input.read_text().splitlines():
    if not line:
        continue
    elif "|" in line:
        RULES.append(tuple(int(r) for r in line.split("|")))
    else:
        pages = [int(p) for p in line.split(",")]
        if correctly_ordered(pages):
            part1 += middle_page(pages)
            continue
        else:
            while not correctly_ordered(pages):
                apply_rules(pages)
            part2 += middle_page(pages)
print(part1)
print(part2)
