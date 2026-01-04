import sys
from hashlib import md5

input = sys.stdin.read().strip()
part1 = 0
part2 = 0
number = 0
while True:
    number += 1
    digest = md5(f"{input}{number}".encode()).hexdigest()
    if digest.startswith("00000") and not part1:
        part1 = number
        print(part1)
    if digest.startswith("000000") and not part2:
        part2 = number
        print(part2)
    if part1 and part2:
        break
