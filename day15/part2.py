from collections import defaultdict
import sys
import heapq


cave = {(int(x), int(y)): int(risk) for y, line in enumerate(sys.stdin)
        for x, risk in enumerate(line.strip())}

edge_x, edge_y = max(cave)
map_expand = 5
max_risk_level = 9


def neighbours(x, y, visited):
    return filter(
        lambda pos: pos[0] >= 0 and pos[0] <= expanded_edge(edge_x)
        and pos[1] >= 0 and pos[1] <= expanded_edge(edge_y)
        and pos not in visited,
        [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    )


def expanded_edge(v):
    return (v+1) * map_expand - 1


q = [(0, 0, 0)]
visited = set()
pos_cost = defaultdict(int)

while len(q) > 0:
    cost, x, y = heapq.heappop(q)

    if (x, y) in visited:
        continue

    visited.add((x, y))
    pos_cost[(x, y)] = cost

    if x == expanded_edge(edge_x) and y == expanded_edge(edge_y):
        break

    for nb_x, nb_y in neighbours(x, y, visited):
        nb_cost = cave[(nb_x % (edge_x + 1), nb_y % (edge_y+1))] + \
            (nb_x // (edge_x+1)) + (nb_y // (edge_y+1))

        # wrap back risk level higher than max risk
        nb_cost = (nb_cost - 1) % max_risk_level + 1

        cost_to = nb_cost + cost
        heapq.heappush(q, (cost_to, nb_x, nb_y))

# result
# sample: 315
# puzzle: 3063
print(pos_cost[(expanded_edge(edge_x), expanded_edge(edge_y))])
