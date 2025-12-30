import sys
from collections.abc import Callable


def paren_solver(expression: str, solver: Callable) -> int:
    left = expression.rfind("(")
    right = expression.find(")", left)
    result = solver(expression[left + 1 : right])
    new = expression[:left] + str(result) + expression[right + 1 :]
    return solver(new)


def operation_solver(words: list[str], index: int) -> None:
    match words[index]:
        case "+":
            result = int(words[index - 1]) + int(words[index + 1])
        case "*":
            result = int(words[index - 1]) * int(words[index + 1])
        case _:
            raise ValueError
    words[index - 1 : index + 2] = [str(result)]


def part1_solver(expression: str) -> int:
    if "(" in expression or ")" in expression:
        return paren_solver(expression, solver=part1_solver)
    words = expression.split()
    while len(words) > 1:
        operation_solver(words, 1)
    return int(words[0])


def part2_solver(expression: str) -> int:
    if "(" in expression or ")" in expression:
        return paren_solver(expression, solver=part2_solver)
    words = expression.split()
    while "+" in words:
        operation_solver(words, words.index("+"))
    while "*" in words:
        operation_solver(words, words.index("*"))
    return int(words[0])


part1 = 0
part2 = 0
input = sys.stdin.read()
for line in input.splitlines():
    part1 += part1_solver(line)
    part2 += part2_solver(line)
print(part1)
print(part2)
