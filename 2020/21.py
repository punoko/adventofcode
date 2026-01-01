import sys

input = sys.stdin.read()
INGREDIENTS: list[str] = []
ALLERGENS: dict[str, set[str]] = {}
for line in input.splitlines():
    str_ingredients, str_allergens = line.split("(contains ")
    ingredients = str_ingredients.split()
    INGREDIENTS.extend(ingredients)
    for allergen in str_allergens.strip(")").split(", "):
        if allergen not in ALLERGENS:
            ALLERGENS[allergen] = set(ingredients)
        else:
            ALLERGENS[allergen].intersection_update(ingredients)

solved = set()
while any(len(ingredients) > 1 for ingredients in ALLERGENS.values()):
    for ingredients in ALLERGENS.values():
        if len(ingredients) > 1:
            ingredients.difference_update(solved)
        if len(ingredients) == 1:
            solved.update(ingredients)

final = [i.pop() for _, i in sorted(ALLERGENS.items())]
part1 = len([i for i in INGREDIENTS if i not in final])
part2 = ",".join(final)
print(part1)
print(part2)
