import sys
from itertools import count
from math import lcm

input = sys.stdin.read().splitlines()

DATE = int(input[0])
BUSES = input[1].split(",")

buses = [int(b) for b in BUSES if b != "x"]
times_until_next = [bus - DATE % bus for bus in buses]
wait = min(times_until_next)
index = times_until_next.index(wait)
bus = buses[index]
print(bus * wait)  # part1

buses = [(i, int(b)) for i, b in enumerate(BUSES) if b != "x"]
timestamp = 1
step = 1
for i, bus in buses:
    # find the next timestamp that works for this bus
    timestamp = next(t for t in count(timestamp, step) if (t + i) % bus == 0)
    # update the step so that each step going forward will still work
    # this is done with the least common multiple of the buses we've processed
    step = lcm(bus, step)
print(timestamp)  # part2
