import sys


def get_invalid_id(a: str, b: str) -> tuple[set[int], set[int]]:
    p1_invalid = set()
    p2_invalid = set()
    for id_len in range(len(a), len(b) + 1):
        for seq_repeat in range(2, len(b) + 1):
            if id_len % seq_repeat != 0:
                continue
            seq_len = id_len // seq_repeat
            seq_min = 10 ** (seq_len - 1) if id_len > len(a) else int(a[:seq_len])
            for seq in range(seq_min, 10**seq_len):
                id = int(str(seq) * seq_repeat)
                if id > int(b):
                    break
                if id >= int(a):
                    if seq_repeat == P1_REPEAT:
                        p1_invalid.add(id)
                    p2_invalid.add(id)
    return p1_invalid, p2_invalid


input = sys.stdin.read()
part1 = 0
part2 = 0

P1_REPEAT = 2
for r in input.split(","):
    a, b = r.strip().split("-")
    p1_invalid, p2_invalid = get_invalid_id(a, b)
    part1 += sum(p1_invalid)
    part2 += sum(p2_invalid)

print(part1)
print(part2)
