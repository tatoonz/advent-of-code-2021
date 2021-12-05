import sys
from collections import defaultdict


def parse_coord(coord):
    x, y = coord.split(',')
    return int(x), int(y)


def find_range(a, b):
    step = 1 if a < b else -1
    return range(a, b + step, step)


diagram = defaultdict(int)

for line in sys.stdin:
    coords = line.strip().split(' -> ')

    x1, y1 = parse_coord(coords[0])
    x2, y2 = parse_coord(coords[1])

    if y1 == y2:
        for x in find_range(x1, x2):
            diagram[(x, y1)] += 1
    elif x1 == x2:
        for y in find_range(y1, y2):
            diagram[(x1, y)] += 1

# result
# sample: 5
# puzzle: 5169
result = sum(1 for k in diagram if diagram[k] > 1)
print(result)
