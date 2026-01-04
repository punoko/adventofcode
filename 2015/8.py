import sys

input = sys.stdin.read()
part1 = 0
part2 = 0

for line in input.splitlines():
    part1 += 2
    encoded = line[1:-1]
    part1 += encoded.count(r"\\")
    encoded = encoded.replace(r"\\", "")
    part1 += encoded.count(r"\"")
    encoded = encoded.replace(r"\"", "")
    part1 += 3 * encoded.count(r"\x")

    part2 += 2
    part2 += line.count("\\")
    part2 += line.count('"')

print(part1)
print(part2)
