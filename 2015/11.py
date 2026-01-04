import sys


def increment_password(password: str) -> str:
    characters = reversed(password)
    result: list[str] = []
    wrap = False
    for i, c in enumerate(characters):
        if i == 0 or wrap:
            char = ALLOWED[ALLOWED.index(c) + 1]
            result.append(char)
            if char == "a":
                wrap = True
                continue
        else:
            result.append(c)
        wrap = False
    return "".join(reversed(result))


def rule1(password: str) -> bool:
    return any(s in password for s in STRAIGHTS)


def rule3(password: str) -> bool:
    copies = []
    for i, c in enumerate(password):
        if i == 0 or c != password[i - 1]:
            copies.append([1, c])
        else:
            copies[-1][0] = copies[-1][0] + 1
    return len([a for a in copies if a[0] > 1]) > 1


ALLOWED = "abcdefghjkmnpqrstuvwxyza"
STRAIGHTS = [ALLOWED[i : i + 3] for i in range(len(ALLOWED) - 3)]

input = sys.stdin.read()
password = input.strip()
part1 = ""
part2 = ""
while True:
    password = increment_password(password)
    if rule1(password) and rule3(password):
        if part1 == "":
            part1 = password
        else:
            part2 = password
            break
print(part1)
print(part2)
