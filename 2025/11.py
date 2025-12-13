import sys
from functools import cache


@cache
def find_out_part1(device: str) -> int:
    if device == "out":
        return 1
    return sum(find_out_part1(dev) for dev in CONNECTIONS[device])


@cache
def find_out_part2(
    device: str,
    seen_dac: bool = False,
    seen_fft: bool = False,
) -> int:
    if device == "out":
        return 1 if (seen_dac and seen_fft) else 0
    if device == "dac":
        seen_dac = True
    elif device == "fft":
        seen_fft = True
    return sum(
        find_out_part2(dev, seen_dac, seen_fft)
        for dev in CONNECTIONS[device]
    )


CONNECTIONS: dict[str, list[str]] = {}
for line in sys.stdin.read().splitlines():
    device, outputs = line.split(":")
    CONNECTIONS[device] = outputs.split()

print(find_out_part1("you"))
print(find_out_part2("svr"))
