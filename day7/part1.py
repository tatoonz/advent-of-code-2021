import sys

input = [int(num) for num in sys.stdin.readline().split(',')]

min_pos = min(input)
max_pos = max(input)

result = sys.maxsize
for i in range(min_pos, max_pos+1):
    total_fuel = sum(abs(num - i) for num in input)
    if total_fuel < result:
        result = total_fuel

print(result)
