import sys
from itertools import chain
from math import prod

type Ticket = tuple[int, ...]
type Ranges = tuple[tuple[int, int], ...]


def parse_ticket_str(ticket_str: str) -> Ticket:
    return tuple(int(n) for n in ticket_str.split(","))


def parse_ranges_str(ranges_str: str) -> Ranges:
    return tuple(
        (int(a), int(b))
        for r in ranges_str.strip().split(" or ")
        for a, b in [r.split("-")]
    )


def value_in_ranges(value: int, ranges: Ranges) -> bool:
    return any(a <= value <= b for a, b in ranges)


input = sys.stdin.read()
_rules, _ticket, _nearby = input.split("\n\n")
rules: dict[str, Ranges] = {
    name: parse_ranges_str(ranges)
    for rule in _rules.splitlines()
    for name, ranges in [rule.split(":")]
}
my_ticket = parse_ticket_str(_ticket.splitlines()[1])
nearby_tickets = [parse_ticket_str(t) for t in _nearby.splitlines()[1:]]

part1_invalid_values: list[int] = []
valid_nearby_tickets: list[Ticket] = []
for ticket in nearby_tickets:
    ticket_invalid_value = [
        value
        for value in ticket
        if not value_in_ranges(value, tuple(chain.from_iterable(rules.values())))
    ]
    if ticket_invalid_value:
        part1_invalid_values.extend(ticket_invalid_value)
    else:
        valid_nearby_tickets.append(ticket)

field_possible_rules: dict[int, set[str]] = {}
for field, field_values in enumerate(zip(*valid_nearby_tickets, strict=True)):
    field_possible_rules[field] = {
        rule
        for rule, ranges in rules.items()
        if all(value_in_ranges(v, ranges) for v in field_values)
    }

available_rules = set(rules)
field_rule: dict[int, str] = {}
for field in sorted(field_possible_rules, key=lambda f: len(field_possible_rules[f])):
    rule = field_possible_rules[field].intersection(available_rules).pop()
    available_rules.remove(rule)
    field_rule[field] = rule

part2_departures = [
    my_ticket[field]
    for field, rule in field_rule.items()
    if rule.startswith("departure")
]

print(sum(part1_invalid_values))
print(prod(part2_departures))
