import re
import sys
from collections import defaultdict

type Data = tuple[int, int, int]  # speed, flying, resting


def position_after_time(speed: int, flying: int, resting: int, time: int) -> int:
    cycles = time // (flying + resting)
    extra = min(flying, time % (flying + resting))
    return speed * (flying * cycles + extra)


def leader_after_time(reindeers: dict[str, Data], time: int) -> tuple[int, str]:
    tmp = [(position_after_time(*data, time), name) for name, data in reindeers.items()]
    return sorted(tmp)[-1]


input = sys.stdin.read()
LIMIT = 2503
REINDEERS: dict[str, Data] = {}
for line in input.splitlines():
    name, data = line.split(maxsplit=1)
    speed, flying, resting = map(int, re.findall(r"\d+", data))
    REINDEERS[name] = (speed, flying, resting)

distance = 0
lead_counter: dict[str, int] = defaultdict(int)
for t in range(1, LIMIT + 1):
    distance, name = leader_after_time(REINDEERS, t)
    lead_counter[name] += 1
part1 = distance
part2 = max(lead_counter.values())

print(part1)
print(part2)
