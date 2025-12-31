import re
import sys
from collections import Counter
from enum import IntEnum
from itertools import chain
from math import prod
from typing import Self


class Tile(tuple[str, ...]):
    """Class providing helpful properties and methods to handle image tiles."""

    __slots__ = ()

    class SIDES(IntEnum):
        """Enum representing the sides of a tile.

        Clockwise order allows for easy rotations.
        """

        top = 0
        right = 1
        bottom = 2
        left = 3

    def flipped(self) -> Self:
        """Tile flipped vertically."""
        return self.__class__(self[::-1])

    def rotated(self, degrees: int) -> Self:
        """Tile rotated by degrees."""
        tmp = self
        for _ in range(degrees // 90 % 4):
            tmp = ["".join(t)[::-1] for t in zip(*tmp, strict=True)]
        return self.__class__(tmp)

    def trimmed(self) -> Self:
        """Tile trimmed by 1 on each side."""
        return self.__class__([row[1:-1] for row in self[1:-1]])

    def oriented(self, border: str, side: SIDES | str) -> Self:
        """Tile rotated and flipped so *border* is facing *side*."""
        if isinstance(side, str):
            side = Tile.SIDES[side]
        try:
            index = self.borders.index(border)
            return self.rotated((side - index) * 90)
        except ValueError:
            flipped = self.flipped()
            index = flipped.borders.index(border)
            return flipped.rotated((side - index) * 90)

    @property
    def top(self) -> str:  # from left to right
        return self[0]

    @property
    def right(self) -> str:  # from top to bottom
        return "".join(line[-1] for line in self)

    @property
    def bottom(self) -> str:  # from right to left
        return self[-1][::-1]

    @property
    def left(self) -> str:  # from bottom to top
        return "".join(line[0] for line in self[::-1])

    @property
    def borders(self) -> tuple[str, str, str, str]:
        return tuple(self.__getattribute__(side.name) for side in Tile.SIDES)


def parse_id(header: str) -> int:
    return int(header.removeprefix("Tile ").rstrip(":"))


def empty_sides(tile: Tile, counter: Counter) -> set[str]:
    return {
        Tile.SIDES(side).name
        for side, border in enumerate(tile.borders)
        if counter[border] == 1
    }


input = sys.stdin.read()
TILES: dict[int, Tile] = {
    parse_id(header): Tile(tile)
    for block in input.split("\n\n")
    for header, *tile in [block.splitlines()]
}

# angles are the tiles for which 2 borders have no match in other tiles
# borders of flipped tiles are included to make sure we match everything
all_borders = [tile.borders + tile.flipped().borders for tile in TILES.values()]
COUNTER = Counter(chain.from_iterable(all_borders))
angles = [id for id, tile in TILES.items() if len(empty_sides(tile, COUNTER)) > 1]
part1 = prod(angles)
print(part1)

# pick one tile from the possible angles and rotate so it can be placed top left
top_left = angles.pop()
remaining = TILES.copy()
remaining.pop(top_left)
sides = empty_sides(tile := TILES[top_left], COUNTER)
if sides == {"top", "right"}:
    TILES[top_left] = tile.rotated(270)
elif sides == {"bottom", "right"}:
    TILES[top_left] = tile.rotated(180)
elif sides == {"bottom", "left"}:
    TILES[top_left] = tile.rotated(90)
elif sides == {"top", "left"}:
    pass
else:
    raise ValueError

# using the top left tile, find the first tile for each row from top to bottom
IMAGE = [[top_left]]
while True:
    found = False
    previous_tile = TILES[IMAGE[-1][0]]
    next_tile_top = previous_tile.bottom[::-1]
    for i, tile in remaining.items():
        try:
            TILES[i] = tile.oriented(next_tile_top, "top")
        except ValueError:
            continue
        found = True
        remaining.pop(i)
        IMAGE.append([i])
        break
    if not found:
        break

# fill the rest of each row from left to right
for row in IMAGE:
    while True:
        found = False
        previous_tile = TILES[row[-1]]
        next_tile_left = previous_tile.right[::-1]
        for i, tile in remaining.items():
            try:
                TILES[i] = tile.oriented(next_tile_left, "left")
            except ValueError:
                continue
            remaining.pop(i)
            row.append(i)
            found = True
            break
        if not found:
            break

# all tiles of the image have been placed, trim and join them into one big sea tile
_sea: list[str] = []
for row in IMAGE:
    trimmed = [TILES[id].trimmed() for id in row]
    lines = zip(*trimmed, strict=True)
    _sea.extend("".join(line) for line in lines)
SEA = Tile(_sea)

# go through every possible orientation of the sea tile and look for monsters
SEA_MONSTER = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]
patterns = [re.compile(string.replace(" ", ".")) for string in SEA_MONSTER]
monster_counter = 0
for angle in (0, 90, 180, 270):
    for face in (SEA, SEA.flipped()):
        sea = face.rotated(angle)
        for row in range(len(sea) - 2):
            col = 0
            while monster0 := patterns[0].search(sea[row], pos=col):
                col = monster0.span(0)[0]
                monster1 = patterns[1].match(sea[row + 1], pos=col)
                monster2 = patterns[2].match(sea[row + 2], pos=col)
                if monster1 and monster2:
                    monster_counter += 1
                col += 1
        # turns out only 1 of 8 orientations has monsters
        if monster_counter:
            break
    if monster_counter:
        break
part2 = "".join(SEA).count("#") - "".join(SEA_MONSTER).count("#") * monster_counter
print(part2)
