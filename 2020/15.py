import sys

input = sys.stdin.read()

PART1 = 2020
PART2 = 30000000
numbers = [int(n) for n in input.strip().split(",")]
history = {n: i + 1 for i, n in enumerate(numbers)}
last = numbers[-1]
for age in range(len(numbers), PART2):
    if age == PART1:
        print(last)  # part1
    next = age - history.get(last, age)
    history[last] = age
    last = next
print(last)  # part2
