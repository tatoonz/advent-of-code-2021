import sys

fish_intervals = [int(interval)
                  for interval in sys.stdin.readline().split(',')]

for n in range(80):
    new_fishes = 0
    for index, interval in enumerate(fish_intervals):
        fish_intervals[index] = interval - 1
        if fish_intervals[index] < 0:
            fish_intervals[index] = 6
            new_fishes += 1

    fish_intervals.extend([8]*new_fishes)

# result
# sample: 5934
# puzzle: 380612
print(len(fish_intervals))
