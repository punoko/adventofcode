import sys

type Deck = list[int]


def combat(player1: Deck, player2: Deck, recursive: bool) -> tuple[Deck, Deck]:
    seen = set()
    while player1 and player2:
        state = (tuple(player1), tuple(player2))
        if recursive and state in seen:
            player2 = []
            break
        seen.add(state)
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        if recursive and len(player1) >= card1 and len(player2) >= card2:
            sub1, _ = combat(player1[:card1], player2[:card2], recursive)
            if sub1:
                player1.extend([card1, card2])
            else:
                player2.extend([card2, card1])
        elif card1 > card2:
            player1.extend([card1, card2])
        else:
            player2.extend([card2, card1])
    return player1, player2


def score(player1: Deck, player2: Deck) -> int:
    winner = reversed(player1) if player1 else reversed(player2)
    return sum(i * card for i, card in enumerate(winner, start=1))


input = sys.stdin.read()
PLAYER1, PLAYER2 = (
    tuple(int(card) for card in block.splitlines()[1:])
    for block in input.split("\n\n")
)
# part 1
p1, p2 = combat(list(PLAYER1), list(PLAYER2), recursive=False)
print(score(p1, p2))
# part2
p1, p2 = combat(list(PLAYER1), list(PLAYER2), recursive=True)
print(score(p1, p2))
