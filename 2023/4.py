INPUT = open("input/4.txt").read()
CARDS = INPUT.splitlines()
part1 = 0
counter = {i: 1 for i in range(len(CARDS))}
for i, card in enumerate(CARDS):
    x, y = (numbers.split() for numbers in card.split(":")[1].split("|"))
    matches = len(set(x) & (set(y)))
    if matches > 0:
        part1 += 2 ** (matches - 1)
    for j in range(matches):
        counter[i + j + 1] += counter[i]
part2 = sum(counter.values())
print(part1)
print(part2)
