from collections import defaultdict
import sys


def count_paths(nodes, current_cave, visited, has_twice_quota=True):
    if current_cave == 'end':
        return 1

    count = 0
    for edge in nodes[current_cave]:
        if not edge.islower() or edge not in visited:
            count += count_paths(nodes, edge, visited |
                                 {edge}, has_twice_quota)
        elif has_twice_quota and edge != 'start' and edge != 'end':
            count += count_paths(nodes, edge, visited |
                                 {edge}, False)

    return count


nodes = defaultdict(list)
for line in sys.stdin:
    src, dest = line.strip().split('-')
    nodes[src].append(dest)
    nodes[dest].append(src)

result = count_paths(nodes, 'start', visited={'start'})

# result
# sample: 3509
# puzzle: 107395
print(result)
