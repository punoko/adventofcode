import math
import sys

type Box = tuple[int, int, int]

input = sys.stdin.read()
part1 = 1
part2 = 0

boxes: list[tuple[int, int, int]] = []
for line in input.splitlines():
    x, y, z = tuple(int(n) for n in line.split(","))
    boxes.append((x, y, z))

junctions: dict[tuple[int, int], float] = {}
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        junctions[(i, j)] = math.dist(boxes[i], boxes[j])

MAX_CONNECTIONS = 1000
shortest = sorted(junctions.items(), key=lambda item: item[1])
shortest = [k for k, v in shortest]

circuits: list[set[int]] = []
for j, pair in enumerate(shortest):
    seen = False
    circuit = set(pair)
    for i, _ in enumerate(circuits):
        if pair[0] in circuits[i] and pair[1] in circuits[i]:
            # both boxes in this pair are already connected to circuit i
            # do nothing
            seen = True
            continue
        elif pair[0] in circuits[i] or pair[1] in circuits[i]:
            # one of our boxes from this pair is connected to circuit i
            # add to the new circuit and clear the old one
            circuit |= circuits[i]
            circuits[i].clear()
    if not seen:
        circuits.append(circuit)
    circuits = [c for c in circuits if c]  # remove empty circuits

    if j == MAX_CONNECTIONS - 1:
        circuits.sort(key=lambda s: len(s), reverse=True)
        for circuit in circuits[:3]:
            part1 *= len(circuit)

    if len(circuits) == 1 and len(circuits[0]) == len(boxes):
        box1_x = boxes[pair[0]][0]
        box2_x = boxes[pair[1]][0]
        part2 = box1_x * box2_x
        break

print(part1)
print(part2)
