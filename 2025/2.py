import sys

input = sys.stdin.read()
part1 = 0
part2 = 0

def check_range(a: str, b: str) -> set[int]:
    invalid = set()

    upper = int("9" * len(a)) + 1
    if upper in range(int(a), int(b) + 1):
        invalid |= check_range(str(upper), b)

    possible_length = [x for x in range(1, len(a) // 2 + 1) if len(a) % x == 0]
    for length in possible_length:
        for pattern in range(int(a[:length]), int("9" * length) + 1):
            num = int(str(pattern) * (len(a) // length))
            if num in range(int(a), min(upper, int(b)) + 1):
                invalid.add(num)
    return invalid

for r in input.split(","):
    a, b = r.strip().split("-")
    invalid = check_range(a, b)
    for n in invalid:
        part2 += n
        nstr = str(n)[: len(str(n)) // 2]
        if str(n) == f"{nstr}{nstr}":
            part1 += n


print(part1)
print(part2)
