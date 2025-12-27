import sys

DIRECTIONS = {
    "N": (0, 1),
    "S": (0, -1),
    "E": (1, 0),
    "W": (-1, 0),
}
input = sys.stdin.read().splitlines()


def rotate(x: int, y: int, rotation: int) -> tuple[int, int]:
    match rotation % 360:
        case 90:
            return y, -x
        case 180:
            return -x, -y
        case 270:
            return -y, x
        case _:
            raise ValueError


def run_instructions(waypoint: tuple[int, int], move: bool) -> None:
    pos_x, pos_y = (0, 0)
    way_x, way_y = waypoint
    for instruction in input:
        action = instruction[0]
        value = int(instruction[1:])
        if action in DIRECTIONS:
            if move:
                pos_x += value * DIRECTIONS[action][0]
                pos_y += value * DIRECTIONS[action][1]
            else:
                way_x += value * DIRECTIONS[action][0]
                way_y += value * DIRECTIONS[action][1]
        elif action == "L":
            way_x, way_y = rotate(x=way_x, y=way_y, rotation=-value)
        elif action == "R":
            way_x, way_y = rotate(x=way_x, y=way_y, rotation=value)
        elif action == "F":
            pos_x += value * way_x
            pos_y += value * way_y
    print(abs(pos_x) + abs(pos_y))


run_instructions(waypoint=(1, 0), move=True)  # part1
run_instructions(waypoint=(10, 1), move=False)  # part2
