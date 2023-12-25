MAP = open("input/10.txt").read().strip().splitlines()
PIPES = {  # maps the direction out of a pipe to its direction coming in
    "|": {"N": "N", "S": "S"},
    "-": {"E": "E", "W": "W"},
    "L": {"W": "N", "S": "E"},
    "J": {"E": "N", "S": "W"},
    "7": {"E": "S", "N": "W"},
    "F": {"W": "S", "N": "E"},
}
R = range(len(MAP))
C = range(len(MAP[0]))


class Snake:
    def __init__(self) -> None:
        self.row = -1
        self.col = -1
        for row in R:
            for col in C:
                if MAP[row][col] == "S":
                    self.row = row
                    self.col = col
                    break
            if self.row in R and self.col in C:
                break
        assert self.row in R and self.col in C
        self.tile = MAP[self.row][self.col]
        self.dir = self.pick_dir()

    def pick_dir(self) -> str:
        for dir in "NSEW":
            if dir in PIPES[self.look(dir)]:
                return dir
        return ""

    def move(self, dir: str | None = None) -> None:
        if dir is None:
            dir = self.dir
        match dir:
            case "N":
                self.row -= 1
            case "S":
                self.row += 1
            case "E":
                self.col += 1
            case "W":
                self.col -= 1
            case _:
                raise ValueError
        self.tile = MAP[self.row][self.col]
        self.dir = PIPES[self.tile][self.dir] if self.tile != "S" else ""

    def look(self, dir: str) -> str:
        match dir:
            case "N":
                return MAP[self.row - 1][self.col]
            case "S":
                return MAP[self.row + 1][self.col]
            case "E":
                return MAP[self.row][self.col + 1]
            case "W":
                return MAP[self.row][self.col - 1]
            case _:
                raise ValueError


snake = Snake()
LOOP = []
while True:
    LOOP.append(snake.tile)
    snake.move()
    if snake.tile == "S":
        break
print(len(LOOP) // 2)
