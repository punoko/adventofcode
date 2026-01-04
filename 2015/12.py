import re
import sys

json = sys.stdin.read().strip()
red = 0
while "{" in json:
    left = json.rfind("{")
    right = json.find("}", left) + 1
    object = json[left:right]
    numbers = re.findall(r"-?\d+", object)
    value = sum(int(n) for n in numbers)
    if r':"red"' in object:
        red += value
        value = 0
    json = json[:left] + str(value) + json[right:]
not_red = int(json)
print(red + not_red)  # part1
print(not_red)  # part2
