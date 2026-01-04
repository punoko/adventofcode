import sys


def solve(signal: str) -> int:
    try:
        return int(signal)
    except ValueError:
        words = signal.split()
    if len(words) == 1:
        result = solve(circuit[signal])
        circuit[signal] = str(result)
    elif words[0] == "NOT":
        result = 2**16 - solve(words[1]) - 1
    elif words[1] == "LSHIFT":
        result = solve(words[0]) << solve(words[2])
    elif words[1] == "RSHIFT":
        result = solve(words[0]) >> solve(words[2])
    elif words[1] == "AND":
        result = solve(words[0]) & solve(words[2])
    elif words[1] == "OR":
        result = solve(words[0]) | solve(words[2])
    else:
        raise ValueError
    return result


input = sys.stdin.read()
CIRCUIT = {v: k for line in input.splitlines() for k, v in [line.split(" -> ")]}

circuit = CIRCUIT.copy()
part1 = solve("a")
print(part1)

circuit = CIRCUIT.copy()
circuit["b"] = str(part1)
part2 = solve("a")
print(part2)
