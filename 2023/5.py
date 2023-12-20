INPUT = open("input/5.txt").read().strip()
s, *maps = [part.split(":")[1].strip() for part in INPUT.split("\n\n")]
s = [int(seed) for seed in s.split()]
part1_seeds = [[s[i], s[i] + 1] for i in range(len(s))]
part2_seeds = [[s[i], s[i] + s[i + 1]] for i in range(0, len(s), 2)]
MAPS = []
for i, _map in enumerate(maps):
    MAPS.append([])
    for line in _map.splitlines():
        MAPS[i].append([int(x) for x in line.split()])


def process(input: list[int], map: list[list[int]]) -> list[list[int]]:
    UNSORTED = [input]
    SORTED = []
    for dst, src, num in map:
        TEMP = []
        y = src + num
        for start, end in UNSORTED:
            left = (start, min(src, end))
            if left[1] > left[0]:
                TEMP.append(left)
            middle = (max(start, src), min(end, y))
            if middle[1] > middle[0]:
                SORTED.append((middle[0] - src + dst, middle[1] - src + dst))
            right = (max(start, y), end)
            if right[1] > right[0]:
                TEMP.append(right)
        UNSORTED = TEMP
    return SORTED + UNSORTED


for source in (part1_seeds, part2_seeds):
    destination = []
    for map in MAPS:
        destination = []
        for input in source:
            destination += process(input, map)
        source = destination
    print(min([min(x) for x in destination]))
