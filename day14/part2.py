# Can't solve by myself
# Solution from: https://www.youtube.com/watch?v=7zvA-o47Uo0
import sys
from collections import Counter, defaultdict

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

C1 = Counter()
for i in range(len(polymer_template)-1):
    C1[polymer_template[i:i+2]] += 1

for _ in range(40):
    C2 = Counter()

    for pair in C1:
        C2[pair[0]+rules[pair]] += C1[pair]
        C2[rules[pair]+pair[1]] += C1[pair]

    C1 = C2


CF = Counter()
for pair in C1:
    CF[pair[0]] += C1[pair]

# Count last character
CF[polymer_template[-1]] += 1

# result
# sample: 2188189693529
# puzzle: 3353146900153
print(max(CF.values()) - min(CF.values()))
