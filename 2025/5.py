import sys

input = sys.stdin.read()
part1 = 0
part2 = 0

temp: list[tuple[int, int]] = []
FRESH: list[tuple[int, int]] = []
INGREDIENTS: list[int] = []
for line in input.splitlines():
    if "-" in line:
        a, b = line.split("-")
        temp.append((int(a), int(b)))
    elif line:
        INGREDIENTS.append(int(line))

temp.sort()
while temp:
    collision = False
    (a, b) = temp.pop()
    for i, (c, d) in enumerate(temp):
        if any(c <= j <= d for j in (a, b)):
            collision = True
            temp[i] = (min(a, c), max(b, d))
            break
    if not collision:
        FRESH.append((a, b))

for i in INGREDIENTS:
    if any(a <= i <= b for a, b in FRESH):
        part1 += 1
for a, b in FRESH:
    part2 += b - a + 1

print(part1)
print(part2)
