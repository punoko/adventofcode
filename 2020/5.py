import sys

input = sys.stdin.read()
part1 = 0
part2 = 0

seats = []
for line in input.splitlines():
    row_str = line[:7]
    col_str = line[7:]
    row = 0
    col = 0
    for i, c in enumerate(reversed(row_str)):
        row += 1 << i if c == "B" else 0
    for i, c in enumerate(reversed(col_str)):
        col += 1 << i if c == "R" else 0
    id = 8 * row + col
    seats.append(id)

part1 = max(seats)
for n in range(part1):
    if n not in seats and ((n - 1) in seats and (n + 1) in seats):
        part2 = n
        break

print(part1)
print(part2)
