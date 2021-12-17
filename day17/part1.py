# Can't solve by myself, learn to solve the problem using math from
# - https://www.reddit.com/r/adventofcode/comments/ri9kdq/2021_day_17_solutions/how8rbd/
# - https://www.reddit.com/r/adventofcode/comments/ri9kdq/2021_day_17_solutions/hovs1jw/
import sys

_, y_range = sys.stdin.readline().strip().replace(
    'target area: ', '').split(', ')

y_min, _ = y_range.replace('y=', '').split('..')
y_min = int(y_min)

# result
# sample: 45
# puzzle: 7626
print(abs(y_min) * (abs(y_min) - 1) / 2)
