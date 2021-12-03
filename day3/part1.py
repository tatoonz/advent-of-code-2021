import sys

# start with make input into 2d array
input = [list(line.rstrip()) for line in sys.stdin]

# sum each column, if total of sum greater than half of the input length
# that means `1` bit is the most common for gamma rate and `0` bit for epsilon rate
gamma_rate_binary = ''
epsilon_rate_binary = ''
for x in range(len(input[0])):
    total = 0
    for y in range(len(input)):
        total += int(input[y][x])

    if total > len(input) / 2:
        gamma_rate_binary += '1'
        epsilon_rate_binary += '0'
    else:
        gamma_rate_binary += '0'
        epsilon_rate_binary += '1'

# result
# sample: 198
# puzzle: 2035764
print(int(gamma_rate_binary, 2) * int(epsilon_rate_binary, 2))
