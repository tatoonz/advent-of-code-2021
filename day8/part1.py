import sys
from collections import Counter

# unique segments
unique_segments = [2, 4, 3, 7]

result = 0
for line in sys.stdin:
    _, output = line.strip().split(' | ')

    for pattern in output.split():
        if len(pattern) in unique_segments:
            result += 1

print(result)
