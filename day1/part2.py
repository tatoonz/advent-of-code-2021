import sys

input = [int(line) for line in sys.stdin]

prevSum = 0
result = 0
for i in range(2, len(input)):
    curSum = input[i] + input[i-1] + input[i-2]
    if prevSum != 0 and curSum > prevSum:
        result += 1

    prevSum = curSum

# result
# sample: 5
# puzzle: 1653
print(result)
