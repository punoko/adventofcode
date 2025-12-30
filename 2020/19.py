import re
import sys


def pattern_cleanup(pattern: str) -> str:
    pattern = pattern.replace(" ", "")
    pattern = pattern.replace("(a)", "a")
    pattern = pattern.replace("(b)", "b")
    return f"^{pattern}$"


def solve_pattern(rules: dict[str, str], max_loops: int = 0) -> str:
    pattern = rules["0"]
    count_8 = max_loops
    count_11 = max_loops
    while any(char not in "ab()| " for char in pattern):
        words = pattern.split()
        seen_8 = False
        seen_11 = False
        for i, word in enumerate(words):
            if word == "8" and count_8:
                words[i] = "( 42 | 42 8 )"
                seen_8 = True
            elif word == "11" and count_11:
                words[i] = "( 42 31 | 42 11 31 )"
                seen_11 = True
            elif word in rules:
                words[i] = f"( {rules[word]} )"
        pattern = " ".join(words)
        count_8 -= seen_8
        count_11 -= seen_11
    return pattern_cleanup(pattern)


input = sys.stdin.read()
rules, messages = input.split("\n\n")
RULES = {
    k: v.replace('"', "")
    for string in rules.splitlines()
    for k, v in [string.split(": ")]
}

part1 = 0
part2 = 0
part1_pattern = re.compile(solve_pattern(RULES))
part2_pattern = re.compile(solve_pattern(RULES, max_loops=5))
for message in messages.splitlines():
    if part1_pattern.match(message):
        part1 += 1
    if part2_pattern.match(message):
        part2 += 1
print(part1)
print(part2)

# first solved part2 by limiting the number of loops to the maximum message length
# found out afterwards the lowest value that workes is 4, using 5 for safety
