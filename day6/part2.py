# Can't solve by myself the for loop from part 1 can't solve for 256 days
#
# so, I learnt some clever solutions from Reddit's threads below:
# using dict: https://www.reddit.com/r/adventofcode/comments/r9z49j/comment/hnfv0qy/?utm_source=reddit&utm_medium=web2x&context=3
# using list: https://www.reddit.com/r/adventofcode/comments/r9z49j/2021_day_6_solutions/hnfd2w5/?utm_source=reddit&utm_medium=web2x&context=3
import sys

data = list(map(int, sys.stdin.readline().split(',')))
fish = [data.count(i) for i in range(9)]

for _ in range(256):
    fish_0_timer = fish[0]

    # decrease fish timer by shift array to the left and use number of fish with zero timer as new breeds
    fish = fish[1:] + [fish_0_timer]

    # also fish with zero timer must reset its timer to 6
    fish[6] += fish_0_timer

# result
# sample: 26984457539
# puzzle: 1710166656900
print(sum(fish))
