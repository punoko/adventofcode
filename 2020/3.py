import sys

input = sys.stdin.read()
part1 = 0
part2 = 1

G = input.splitlines()
R = len(G)
C = len(G[0])

for right, down in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
    row = 0
    col = 0
    trees = 0
    while row < R:
        if G[row][col] == "#":
            trees += 1
        row += down
        col += right
        col %= C
    if (right, down) == (3, 1):
        part1 = trees
    part2 *= trees

print(part1)
print(part2)
