import sys
import math

cave = {(int(x), int(y)): int(risk) for y, line in enumerate(sys.stdin)
        for x, risk in enumerate(line.strip())}

max_x = max(x for x, _ in cave.keys())
max_y = max(y for _, y in cave.keys())

# don't count risk level at starting point
cave[(0, 0)] = 0
cache = {}


def find_min_risk(x, y):
    if (x, y) in cache:
        return cache[(x, y)]

    if (x, y) not in cave:
        return math.inf

    if x == max_x and y == max_y:
        return cave[(x, y)]

    cache[(x, y)] = cave[(x, y)] + \
        min(find_min_risk(x+1, y), find_min_risk(x, y+1))

    return cache[(x, y)]


# result
# sample: 40
# puzzle: 824
print(find_min_risk(0, 0))
