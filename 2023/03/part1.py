import re

SCHEMATIC = open("input.txt", "r").read().splitlines()
HEIGHT = len(SCHEMATIC)
WIDTH = len(SCHEMATIC[0])

class EnginePart:
    def __init__(self, number: str, col: int, row: int):
        self.number = number
        self.col = col
        self.row = row

        self.up = max(self.row - 1, 0)
        self.down = min(self.row + 1, HEIGHT - 1)
        self.left = max(self.col - 1, 0)
        self.right = min(self.col + len(self), WIDTH - 1)

        self.neighbours = []
        for y in range(self.up, self.down + 1):
            self.neighbours.append(SCHEMATIC[y][self.left : self.right + 1])

    def __len__(self):
        return len(self.number)

    def __str__(self):
        return "\n".join(self.neighbours)

    def is_valid(self):
        if re.search(r"[^0-9.]", "".join(self.neighbours)):
            return True
        else:
            return False

answer = 0
for index, string in enumerate(SCHEMATIC):
    matches = re.finditer("\d+", string)
    for match in matches:
        part = EnginePart(match.group(), match.start(), index)
        if part.is_valid():
            answer += int(part.number)
print(answer)
