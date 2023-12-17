INPUT = open("input/3.txt").read()
GRID = INPUT.splitlines()
ROWS = len(GRID)
COLS = len(GRID[0])
part1 = 0
part2 = 0
numbers = {}
for row in range(ROWS):
    number = 0
    valid = False
    gears = set()
    for col in range(COLS+1):
        if col < COLS and GRID[row][col].isdigit():
            number = number * 10 + int(GRID[row][col])
            for r in (-1, 0, 1):
                for c in (-1, 0, 1):
                    if 0 <= row+r < ROWS and 0 <= col+c < COLS:
                        ch = GRID[row+r][col+c]
                        if not ch.isdigit() and ch != '.':
                            valid = True
                        if ch == '*':
                            gears.add((row+r, col+c))
        elif number > 0:
            for gear in gears:
                numbers.setdefault(gear, []).append(number)
            gears.clear()
            if valid:
                part1 += number
            number = 0
            valid = False
for gear in numbers:
    if len(numbers[gear]) == 2:
        part2 += numbers[gear][0] * numbers[gear][1]
print(part1)
print(part2)
