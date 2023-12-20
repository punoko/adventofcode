INPUT = open("input/7.txt").read().strip()
HIGH = 0
PAIR = 1
PAIRS = 2
THREE = 3
FULL = 4
FOUR = 5
FIVE = 6


def get_values(hand: str) -> tuple[int, int]:
    counter = {}
    for card in hand:
        counter[card] = 1 + counter.get(card, 0)
    joker = counter.get("J", 0)
    match len(counter):
        case 5:
            return HIGH, PAIR if joker else HIGH
        case 4:
            return PAIR, THREE if joker else PAIR
        case 3:
            if 2 in counter.values():
                if joker == 2:
                    return PAIRS, FOUR
                elif joker == 1:
                    return PAIRS, FULL
                else:
                    return PAIRS, PAIRS
            else:
                return THREE, FOUR if joker else THREE
        case 2:
            if 2 in counter.values():
                return FULL, FIVE if joker else FULL
            else:
                return FOUR, FIVE if joker else FOUR
        case 1:
            return FIVE, FIVE
        case _:
            assert False


HANDS = [line.split() for line in INPUT.splitlines()]
TABLE = str.maketrans("TJQKA", "abcde")
part1 = [[] for i in range(7)]
part2 = [[] for i in range(7)]
for hand, bid in HANDS:
    bid = int(bid)
    value1, value2 = get_values(hand)
    hand = hand.translate(TABLE)
    part1[value1].append((hand, bid))
    hand = hand.replace("b", "1")
    part2[value2].append((hand, bid))

for part in [part1, part2]:
    i = 0
    score = 0
    for group in part:
        for hand, bid in sorted(group):
            i += 1
            score += i * bid
    print(score)
