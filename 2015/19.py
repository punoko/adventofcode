import sys

input = sys.stdin.read()
_replacements, _medicine = input.split("\n\n")
medicine = _medicine.strip()
replacements: set[tuple[str, str]] = {
    (src, dst)
    for replacement in _replacements.splitlines()
    for src, dst in [replacement.split(" => ")]
}

part1_mollecules = set()
for src, dst in replacements:
    index = 0
    while True:
        try:
            index = medicine.index(src, index)
        except ValueError:
            break
        tmp = medicine[:index] + medicine[index:].replace(src, dst, count=1)
        part1_mollecules.add(tmp)
        index += 1
print(len(part1_mollecules))  # part1

part2_steps = 0
# sort replacements by longest output string to minimize steps
sorted_replacements = sorted(replacements, key=lambda x: len(x[1]), reverse=True)
while medicine != "e":
    for src, dst in sorted_replacements:
        index = 0
        while True:
            try:
                index = medicine.index(dst, index)
            except ValueError:
                break
            medicine = medicine[:index] + medicine[index:].replace(dst, src, count=1)
            part2_steps += 1
print(part2_steps)  # part2
