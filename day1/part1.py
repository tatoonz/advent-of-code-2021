import sys

input = []
for line in sys.stdin:
    input.append(int(line))

result = 0
index = 1
while index < len(input):
    if input[index-1] < input[index]:
        result += 1

    index += 1

print(result)
