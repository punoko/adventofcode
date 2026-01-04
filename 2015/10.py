import sys


def look_and_say(digits: list[int]) -> list[int]:
    result = []
    for i, n in enumerate(digits):
        if i == 0 or n != digits[i - 1]:
            result.extend([1, n])
        else:
            result[-2] = result[-2] + 1
    return result


input = sys.stdin.read()
result = [int(n) for n in input.strip()]

for _ in range(40):
    result = look_and_say(result)
print(len(result))  # part1

for _ in range(10):
    result = look_and_say(result)
print(len(result))  # part2
