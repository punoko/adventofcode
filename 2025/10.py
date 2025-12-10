import sys
from functools import reduce
from itertools import chain, combinations
from operator import xor


def encode_to_binary(bits: tuple[int, ...]) -> int:
    return sum(1 << pos for pos in bits)


input = sys.stdin.read()
part1 = 0
part2 = 0

for _, line in enumerate(input.splitlines()):
    light_str, *buttons_str, joltage_str = line.split()

    light_tuple = tuple(i for i, c in enumerate(light_str[1:-1]) if c == "#")
    buttons_tuples = [tuple(int(n) for n in b[1:-1].split(",")) for b in buttons_str]
    joltage_tuple = tuple(int(i) for i in joltage_str[1:-1].split(","))

    # generating binary representation for buttons and lights
    # so we can simply toggle buttons with XOR
    light_int = encode_to_binary(light_tuple)
    buttons_ints = [encode_to_binary(b) for b in buttons_tuples]
    # with lights, button presses are toggles so pressing a button twice does nothing
    # buttons should be pressed at most once
    for button_combination in chain.from_iterable(
        combinations(buttons_ints, n) for n in range(1, len(buttons_ints) + 1)
    ):
        if reduce(xor, button_combination) == light_int:
            part1 += len(button_combination)
            break

print(part1)
print(part2)
