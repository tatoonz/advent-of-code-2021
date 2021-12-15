# Can't solve by myself
# Solution from: https://www.youtube.com/watch?v=7zvA-o47Uo0
import sys
from collections import Counter

polymer_template = ''
rules = {}

for line in sys.stdin:
    line = line.strip()
    if line == '':
        continue

    if '->' in line:
        pair, elem = line.split(' -> ')
        rules[pair] = elem
    else:
        polymer_template = line

for _ in range(10):
    temp_template = ''
    for i in range(len(polymer_template)):
        temp_template += polymer_template[i]

        if i+1 < len(polymer_template):
            temp_template += rules[polymer_template[i] + polymer_template[i+1]]

    polymer_template = temp_template

c = Counter(polymer_template)

# result
# sample: 1588
# puzzle: 2915
print(max(c.values()) - min(c.values()))
