import re
import sys
from itertools import product


def int_to_bits(integer: int) -> list[str]:
    return list(f"{integer:b}".rjust(36, "0"))


def bits_to_int(binary: list[str]) -> int:
    return int("".join(binary), 2)


input = sys.stdin.read()
mask = ""
part1_memory = {}
part2_memory = {}
for line in input.splitlines():
    if match := re.match(r"mask = ([X01]{36})", line):
        mask = match.group(1)
    elif match := re.match(r"mem\[(\d+)\] = (\d+)", line):
        address, value = map(int, match.groups())
        part1_value = int_to_bits(value)
        part2_address = int_to_bits(address)
        floating_bits = []
        for i, char in enumerate(mask):
            if char == "1":
                part2_address[i] = "1"
            if char == "X":
                floating_bits.append(i)
            else:
                part1_value[i] = char
        for p in product("01", repeat=len(floating_bits)):
            for i, j in enumerate(floating_bits):
                part2_address[j] = p[i]
            part2_memory[bits_to_int(part2_address)] = value
        part1_memory[address] = bits_to_int(part1_value)
print(sum(part1_memory.values()))
print(sum(part2_memory.values()))
