import sys


def calc_fuel_cost(guess_position, crab_positions):
    result = 0
    for crab_position in crab_positions:
        steps = abs(crab_position - guess_position)
        result += int(steps * (steps + 1) / 2)

    return result


input = [int(num) for num in sys.stdin.readline().split(',')]

min_position = min(input)
max_position = max(input)

result = 0
while min_position < max_position:
    mid_position = int((min_position + max_position) / 2)

    fuel_cost_left = calc_fuel_cost(mid_position, input)
    fuel_cost_right = calc_fuel_cost(mid_position+1, input)

    if fuel_cost_left < fuel_cost_right:
        result = fuel_cost_left
        max_position = mid_position
    elif fuel_cost_left > fuel_cost_right:
        result = fuel_cost_right
        min_position = mid_position + 1

# result
# sample: 168
# puzzle: 96361606
print(result)
