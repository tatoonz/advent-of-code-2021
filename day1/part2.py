import sys

input = []
for line in sys.stdin:
    input.append(int(line))

threeMeasurement = []
index = 2
while index < len(input):
    threeMeasurement.append(input[index] + input[index-1] + input[index-2])
    index += 1

result = 0
index = 1
while index < len(threeMeasurement):
    if threeMeasurement[index-1] < threeMeasurement[index]:
        result += 1

    index += 1

print(result)
