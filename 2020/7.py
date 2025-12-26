import re
import sys
from collections import defaultdict


def can_contain(bag: str) -> set[str]:
    bags = set()
    for parent in RULES:
        if bag in RULES[parent]:
            bags.add(parent)
            bags.update(can_contain(parent))
    return bags


def must_be_contained_in(bag: str, top_level: bool = True) -> int:
    if not RULES[bag]:
        return 1
    bags = 0
    for child, num in RULES[bag].items():
        bags += num * must_be_contained_in(child, False)
    if not top_level:
        bags += 1
    return bags


input = sys.stdin.read()
part1 = 0
part2 = 0

RULES = defaultdict(dict)
for line in input.splitlines():
    if "no other" in line:
        continue
    clean, _ = re.subn(r" bags?\.?", "", line)
    parent, children = clean.split("contain ")
    RULES[parent.strip()] = {
        bag.strip(): int(num)
        for s in children.split(",")
        for num, bag in [s.strip().split(maxsplit=1)]
    }

part1 = len(can_contain("shiny gold"))
part2 = must_be_contained_in("shiny gold")


print(part1)
print(part2)
