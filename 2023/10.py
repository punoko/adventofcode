import sys

SOUTH = (1, 0)
NORTH = (-1, 0)
EAST = (0, 1)
WEST = (0, -1)
CONNECTIONS = {
    "|": (NORTH, SOUTH),
    "-": (EAST, WEST),
    "L": (NORTH, EAST),
    "J": (NORTH, WEST),
    "7": (SOUTH, WEST),
    "F": (SOUTH, EAST),
}

input = sys.stdin.read()
G = input.splitlines()
R = len(G)
C = len(G[0])
LOOP = set()

# find start
r, c = next((r, c) for r in range(R) for c in range(C) if G[r][c] == "S")
LOOP.add((r, c))

# pick first step
if G[r - 1][c] in ("|", "7", "F"):
    r -= 1  # go north
elif G[r + 1][c] in ("|", "L", "J"):
    r += 1  # go south
elif G[r][c + 1] in ("-", "J", "7"):
    c += 1  # go east
elif G[r][c - 1] in ("-", "L", "F"):
    c -= 1  # go west
LOOP.add((r, c))

while True:  # go through loop
    connections = [(r + rr, c + cc) for rr, cc in CONNECTIONS[G[r][c]]]
    try:
        r, c = next((r, c) for r, c in connections if (r, c) not in LOOP)
        LOOP.add((r, c))
    except StopIteration:
        break

part1 = len(LOOP) // 2
print(part1)
