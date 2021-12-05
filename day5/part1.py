import sys
from collections import defaultdict


def parse_coord(coord):
    x, y = coord.split(',')
    return int(x), int(y)


diagram = defaultdict(int)

for line in sys.stdin:
    coords = line.strip().split(' -> ')

    x1, y1 = parse_coord(coords[0])
    x2, y2 = parse_coord(coords[1])

    if y1 == y2:
        step = 1 if x1 < x2 else -1
        for x in range(x1, x2 + step, step):
            diagram[(x, y1)] += 1
    elif x1 == x2:
        step = 1 if y1 < y2 else -1
        for y in range(y1, y2 + step, step):
            diagram[(x1, y)] += 1

# result
# sample: 5
# puzzle: 5169
result = sum(1 for k in diagram if diagram[k] > 1)
print(result)
