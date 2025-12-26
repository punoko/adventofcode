import sys


def run(
    code: list[str],
    offset: int = 0,
    accumulator: int = 0,
    end: bool = False,
) -> tuple[int, bool]:
    seen: list[int] = []
    while True:
        if offset in seen:
            break  # reached infinite loop
        if offset == len(code):
            end = True
            break  # reached the end
        seen.append(offset)
        operation, argument = code[offset].split()
        if operation == "acc":
            accumulator += int(argument)
            offset += 1
        elif operation == "jmp":
            offset += int(argument)
        elif operation == "nop":
            offset += 1
    return accumulator, end


CODE = sys.stdin.readlines()

part1, _ = run(code=CODE)
part2 = 0
for i, instruction in enumerate(CODE):
    if instruction.startswith("nop"):
        new = instruction.replace("nop", "jmp")
    elif instruction.startswith("jmp"):
        new = instruction.replace("jmp", "nop")
    else:  # acc
        continue
    program = CODE.copy()
    program[i] = new
    acc, end = run(code=program)
    if end:
        part2 = acc
        break

print(part1)
print(part2)
