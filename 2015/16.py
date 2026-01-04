import sys

input = sys.stdin.read()
part1 = 0
part2 = 0

MFCSAM = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}
SUES = 500
for line in input.splitlines():
    sue, data = line.split(": ", maxsplit=1)
    found_p1 = True
    found_p2 = True
    for item in data.split(", "):
        name, value = item.split(": ")
        value = int(value)
        if MFCSAM[name] != value:
            found_p1 = False
        if name in ("cats", "trees"):
            if MFCSAM[name] >= value:
                found_p2 = False
        elif name in ("pomeranians", "goldfish"):
            if MFCSAM[name] <= value:
                found_p2 = False
        elif MFCSAM[name] != value:
            found_p2 = False
    if found_p1:
        part1 = sue
    if found_p2:
        part2 = sue

print(part1)
print(part2)
