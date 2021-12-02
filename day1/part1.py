# improved code, many thanks to this Reddit's comment: (i'm new to python)
# https://www.reddit.com/r/adventofcode/comments/r66vow/comment/hmwtvis/?utm_source=reddit&utm_medium=web2x&context=3
import sys

input = [int(line) for line in sys.stdin]

# zip(input, input[1:]) if based on sample input, the output is:
# [(199, 200), (200, 208), (208, 210), (210, 200), (200, 207), (207, 240), (240, 269), (269, 260), (260, 263)]
#
# So, when you do loop a and b will be
# 1. a=199, b=200
# 2. a=200, b=208
# 3. a=208, b=210
# 4. and so on...
result = sum(b > a for a, b in zip(input, input[1:]))
print(result)
