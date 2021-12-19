import sys
from math import sqrt

x_range, y_range = sys.stdin.readline().strip().replace(
    'target area: ', '').split(', ')

x_min, x_max = x_range.replace('x=', '').split('..')
x_min, x_max = int(x_min), int(x_max)

y_min, y_max = y_range.replace('y=', '').split('..')
y_min, y_max = int(y_min), int(y_max)


# solution from: https://github.com/SuddenGunter/adventofcode/blob/main/2021/day17/task2/solver.go#L92
def x_lower_bound(x_min, x_max):
    a = b = 1
    min_reachable_x = x_min

    while min_reachable_x <= x_max:
        c = -(min_reachable_x) * 2
        possible_x = (-b + sqrt(b*b-4*a*c)) / 2

        if possible_x == int(possible_x):
            return int(possible_x)

        min_reachable_x += 1

    return 0


def y_upper_bound(y_min):
    return int(abs(y_min) * (abs(y_min) - 1) / 2)


result = 0
for x in range(x_lower_bound(x_min, x_max), x_max + 1):
    for y in range(y_min, y_upper_bound(y_min) + 1):
        x_pos = x_velo = x
        y_pos = y_velo = y

        while x_pos <= x_max and y_pos >= y_min:
            if (
                x_min <= x_pos <= x_max
                and y_min <= y_pos <= y_max
            ):
                result += 1
                break

            x_velo = max(0, x_velo - 1)
            y_velo -= 1

            x_pos += x_velo
            y_pos += y_velo

# result
# sample: 112
# puzzle: 2032
print(result)
