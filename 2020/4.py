# ruff: noqa: PLR2004
import re
import sys

input = sys.stdin.read()
part1 = 0
part2 = 0

REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
for passport in input.split("\n\n"):
    data = dict(string.split(":") for string in sorted(passport.split()))
    if set(data.keys()) >= REQUIRED_FIELDS:
        part1 += 1
        hgt_cm = (
            int(data["hgt"].removesuffix("cm"))
            if data["hgt"].endswith("cm")
            else 0
        )
        hgt_in = (
            int(data["hgt"].removesuffix("in"))
            if data["hgt"].endswith("in")
            else 0
        )
        if (
            1920 <= int(data["byr"]) <= 2002
            and 2010 <= int(data["iyr"]) <= 2020
            and 2020 <= int(data["eyr"]) <= 2030
            and (150 <= hgt_cm <= 193 or 59 <= hgt_in <= 76)
            and re.match(r"#[0-9a-f]{6}", data["hcl"])
            and data["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
            and re.match(r"^[0-9]{9}$", data["pid"])
        ):
            part2 += 1

print(part1)
print(part2)
