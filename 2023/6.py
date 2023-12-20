INPUT = open("input/6.txt").read().strip()
TIME, DISTANCE = [line.split(":")[1].split() for line in INPUT.splitlines()]
p1_input = [(int(TIME[i]), int(DISTANCE[i])) for i in range(len(TIME))]
p2_input = [(int("".join(TIME)), int("".join(DISTANCE)))]
for input in [p1_input, p2_input]:
    output = []
    score = 1
    for time, distance in input:
        button_min = 0
        while button_min * (time - button_min) <= distance:
            button_min += 1
        button_max = time
        while button_max * (time - button_max) <= distance:
            button_max -= 1
        output.append(len(range(button_min, button_max + 1)))
    for num in output:
        score *= num
    print(score)
