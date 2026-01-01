import sys

input = sys.stdin.read()
CUPS = tuple(int(n) for n in input.strip())
LEN = len(CUPS)
MOVES = 100
cups = list(CUPS)
current = cups[0]
for _ in range(MOVES):
    i = cups.index(current)
    removed = (cups + cups)[i + 1 : i + 4]
    for label in removed:
        cups.remove(label)
    destination = current - 1
    while destination not in cups:
        destination -= 1
        if destination < min(CUPS):
            destination = max(CUPS)
    j = cups.index(destination) + 1
    cups[j:j] = removed
    k = (cups.index(current) + 1) % LEN
    current = cups[k]
one = cups.index(1)
final = (cups[one:] + cups[:one])[1:]
print("".join(map(str, final)))
