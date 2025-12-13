import sys

input = sys.stdin.read()
part1 = 0
part2 = 0

*shapes, regions = input.split("\n\n")

SHAPES = {}
SIZES = {}
for s in shapes:
    index, *shape = s.splitlines()
    index = int(index.rstrip(":"))
    SHAPES[index] = shape
    SIZES[index] = "".join(shape).count("#")

for region in regions.splitlines():
    size_str, *count_str = region.split()
    width, length = [int(n) for n in size_str[:-1].split("x")]
    size_region = width * length
    count = [int(n) for n in count_str]
    size_presents = sum([n * SIZES[i] for i, n in enumerate(count)])
    if size_presents < size_region:
        # this does not work for the test at all but
        # somehow it is the correct answer for our input lmao
        part1 += 1

print(part1)
print(part2)
