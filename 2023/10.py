import sys

SOUTH = (1, 0)
NORTH = (-1, 0)
EAST = (0, 1)
WEST = (0, -1)
CONNECTIONS = {
    "|": {NORTH, SOUTH},
    "-": {EAST, WEST},
    "L": {NORTH, EAST},
    "J": {NORTH, WEST},
    "7": {SOUTH, WEST},
    "F": {SOUTH, EAST},
}

input = sys.stdin.read()
G = input.splitlines()
R = len(G)
C = len(G[0])
LOOP = set()

# find start
r, c = next((r, c) for r in range(R) for c in range(C) if G[r][c] == "S")
LOOP.add((r, c))

# replace S with its actual pipe shape so we can solve part2
S_connections = set()
if G[r - 1][c] in ("|", "7", "F"):
    S_connections.add(NORTH)
if G[r + 1][c] in ("|", "L", "J"):
    S_connections.add(SOUTH)
if G[r][c + 1] in ("-", "J", "7"):
    S_connections.add(EAST)
if G[r][c - 1] in ("-", "L", "F"):
    S_connections.add(WEST)
S = next(k for k, v in CONNECTIONS.items() if S_connections == v)
G[r] = G[r].replace("S", S)

# pick any of the two S connections as first step
rr, cc = S_connections.pop()
r += rr
c += cc
LOOP.add((r, c))

# go through loop
while True:
    connections = [(r + rr, c + cc) for rr, cc in CONNECTIONS[G[r][c]]]
    try:
        r, c = next((r, c) for r, c in connections if (r, c) not in LOOP)
        LOOP.add((r, c))
    except StopIteration:
        break

part1 = len(LOOP) // 2
print(part1)

part2 = 0
for r in range(R):
    inside = False
    entry = None
    for c in range(C):
        tile = G[r][c]
        if (r, c) not in LOOP:
            if inside:
                part2 += 1
        elif tile in ("F", "L"):
            entry = tile
        elif (
            tile == "|"
            or (entry == "L" and tile == "7")
            or (entry == "F" and tile == "J")
        ):
            inside = not inside
print(part2)
