import sys


def transform(value: int, subject_number: int) -> int:
    return value * subject_number % 20201227


def find_loop_size(public_key: int, subject_number: int = 7) -> int:
    value = 1
    loop_size = 0
    while value != public_key:
        loop_size += 1
        value = transform(value, subject_number)
    return loop_size


input = sys.stdin.read()
card_pub, door_pub = [int(line) for line in input.splitlines()]
card_loop_size = find_loop_size(card_pub)
door_loop_size = find_loop_size(door_pub)

encryption_key = 1
for _ in range(door_loop_size):
    encryption_key = transform(encryption_key, subject_number=card_pub)
print(encryption_key)  # part1
