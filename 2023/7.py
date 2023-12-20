INPUT = open("input/7.txt").read().strip()
TABLE = str.maketrans("TJQKA", "abcde")
HIGH, PAIR, PAIRS, THREE, FULL, FOUR, FIVE = 0, 1, 2, 3, 4, 5, 6


def strength(hand: str, JOKER: bool) -> tuple[int, str]:
    counter = {}
    for card in hand:
        counter[card] = 1 + counter.get(card, 0)
    joker = counter.get("b", 0) * JOKER
    match len(counter):
        case 5:
            value = PAIR if joker else HIGH
        case 4:
            value = THREE if joker else PAIR
        case 3:
            if 2 in counter.values():
                if joker == 2:
                    value = FOUR
                elif joker == 1:
                    value = FULL
                else:
                    value = PAIRS
            else:
                value = FOUR if joker else THREE
        case 2:
            if 2 in counter.values():
                value = FIVE if joker else FULL
            else:
                value = FIVE if joker else FOUR
        case 1:
            value = FIVE
        case _:
            assert False
    return value, hand.replace("b", "1") if JOKER else hand


HANDS = []
for hand, bid in [line.split() for line in INPUT.splitlines()]:
    HANDS.append((hand.translate(TABLE), int(bid)))
for JOKER in (False, True):
    score = 0
    HANDS.sort(key=lambda hb: strength(hb[0], JOKER))
    for i, (hand, bid) in enumerate(HANDS):
        score += bid * (i + 1)
    print(score)
