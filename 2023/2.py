import sys
INPUT = open(sys.argv[1]).read()
part1 = 0
part2 = 0
for game in INPUT.splitlines():
    minimum = {}
    possible = True
    power = 1
    id, sets = game.split(':')
    for set in sets.split(';'):
        for balls in set.split(','):
            count, color = balls.split()
            count = int(count)
            if count > {'red': 12, 'green': 13, 'blue': 14}[color]:
                possible = False
            minimum[color] = max(count, minimum.get(color, 1))
    if possible:
        part1 += int(id.split()[-1])
    for value in minimum.values():
        power *= value
    part2 += power
print(part1)
print(part2)
