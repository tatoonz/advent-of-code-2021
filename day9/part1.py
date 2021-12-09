import sys


def get_top(input, x, y):
    topY = y - 1
    if topY < 0:
        return sys.maxsize
    return input[topY][x]


def get_right(input, x, y):
    rightX = x + 1
    if rightX > len(input[y]) - 1:
        return sys.maxsize
    return input[y][rightX]


def get_bottom(input, x, y):
    bottomY = y + 1
    if bottomY > len(input) - 1:
        return sys.maxsize
    return input[bottomY][x]


def get_left(input, x, y):
    leftX = x - 1
    if leftX < 0:
        return sys.maxsize
    return input[y][leftX]


input = [[int(num) for num in list(line.strip())] for line in sys.stdin]

low_points = []

for y in range(len(input)):
    for x in range(len(input[0])):
        current_height = input[y][x]

        if (
            current_height < get_top(input, x, y)
            and current_height < get_right(input, x, y)
            and current_height < get_bottom(input, x, y)
            and current_height < get_left(input, x, y)
        ):
            low_points.append(current_height+1)

# result
# sample: 15
# puzzle: 585
print(sum(low_points))
