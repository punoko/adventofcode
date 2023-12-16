import sys
INPUT = open(sys.argv[1]).read()
part1 = 0
part2 = 0
for line in INPUT.splitlines():
    digits1 = []
    digits2 = []
    for i, char in enumerate(line):
        if char.isdigit():
            digits1.append(char)
            digits2.append(char)
        for j, letters in enumerate(('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')):
            if line[i:].startswith(letters):
                digits2.append(str(j+1))
    part1 += int(digits1[0] + digits1[-1])
    part2 += int(digits2[0] + digits2[-1])
print(part1)
print(part2)
