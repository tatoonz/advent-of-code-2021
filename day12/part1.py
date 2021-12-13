from collections import defaultdict
import sys


def count_paths(nodes, current_cave, visited):
    if current_cave == 'end':
        return 1

    return sum(count_paths(nodes, edge, visited | {edge}) for edge in nodes[current_cave] if edge not in visited or not edge.islower())


nodes = defaultdict(list)
for line in sys.stdin:
    src, dest = line.strip().split('-')
    nodes[src].append(dest)
    nodes[dest].append(src)

result = count_paths(nodes, 'start', visited={'start'})

# result
# sample: 226
print(result)
