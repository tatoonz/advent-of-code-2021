# Can't solve by my self
# Solution from: https://www.reddit.com/r/adventofcode/comments/rca6vp/comment/hnumswo/?utm_source=reddit&utm_medium=web2x&context=3
import sys
from math import prod


def neighbours(input, x, y):
    return filter(lambda x: x in input, [(x, y-1), (x+1, y), (x, y+1), (x-1, y)])


def is_low(input, current_pos):
    return all(input[current_pos] < input[x] for x in neighbours(input, *current_pos))


input = {(x, y): int(h) for y, line in enumerate(sys.stdin)
         for x, h in enumerate(line.strip())}

# can convert for-loop below to:
# low_points = list(filter(lambda pos: is_low(input, pos), input))
low_points = []
for current_pos in input:
    if is_low(input, current_pos):
        low_points.append(current_pos)


def count_basin(input, pos):
    if input[pos] == 9:
        return 0

    # remove visited position
    del input[pos]

    # plus 1 to including the low point
    return 1 + sum(map(lambda neighbour_pos: count_basin(input, neighbour_pos), neighbours(input, *pos)))


basins = [count_basin(input, pos) for pos in low_points]

# result
# sample: 1134
# puzzle: 827904
print(prod(sorted(basins)[-3:]))
