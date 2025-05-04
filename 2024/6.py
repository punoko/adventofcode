# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from itertools import cycle
from pathlib import Path
from enum import Enum


class Direction(Enum):
    U = (0, -1)
    R = (1, 0)
    D = (0, 1)
    L = (-1, 0)


class Guard:
    def __init__(self, x: int, y: int) -> None:
        self._cycle = cycle(Direction)
        self.pos = x, y
        self.dir = next(self._cycle)

    def turn(self) -> None:
        self.dir = next(self._cycle)

    def next(self) -> tuple[int, int]:
        return self.pos[0] + self.dir.value[0], self.pos[1] + self.dir.value[1]

    def move(self) -> None:
        self.pos = self.next()


def get(x: int, y: int) -> str | None:
    global lines
    if x < 0 or x >= X_MAX or y < 0 or y >= Y_MAX:
        return None
    else:
        return lines[y][x]


def mark(x: int, y: int, char: str) -> None:
    global lines
    line = list(lines[y])
    line[x] = char
    lines[y] = "".join(line)


input = Path("input", Path(__file__).name).with_suffix(".txt")
LINES = tuple(input.read_text().splitlines())
Y_MAX = len(LINES)
X_MAX = len(LINES[0])
START = None
for y, line in enumerate(LINES):
    if "^" in line:
        START = (line.index("^"), y)
        break
if START is None:
    exit(1)

part1 = 0
lines = list(LINES)
guard = Guard(*START)
while get(*guard.pos):
    if get(*guard.next()) == "#":
        guard.turn()
    else:
        mark(*guard.pos, char=guard.dir.name)
        guard.move()
total = "".join(lines)
for char in "URDL":
    part1 += total.count(char)
print(part1)

part2 = 0
for y, line in enumerate(LINES):
    for x, _ in enumerate(line):
        print((x, y))
        if (x, y) == START:
            continue
        lines = list(LINES)
        mark(x, y, "#")
        guard = Guard(*START)
        count = 0
        while get(*guard.pos):
            if get(*guard.next()) == "#":
                guard.turn()
            elif get(*guard.next()) == guard.dir.name:
                print("loop")
                part2 += 1
                break
            elif count > 10000:
                # dirty hack because this implementation breaks
                # when the loop is on a straight line lol
                print("loop lol")
                part2 += 1
                break
            else:
                count += 1
                mark(*guard.pos, char=guard.dir.name)
                guard.move()
print(part2)
