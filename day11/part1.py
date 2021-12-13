import sys


def neighbours(grid, x, y):
    return filter(lambda pos: pos in grid, [
        (x-1, y-1), (x, y-1), (x+1, y-1),
        (x-1, y), (x+1, y),
        (x-1, y+1), (x, y+1), (x+1, y+1),
    ])


def gain_energy(grid, pos, flashed_pos):
    if pos not in flashed_pos:
        grid[pos] += 1

    flashes = 0
    if grid[pos] > 9:
        grid[pos] = 0
        flashed_pos[pos] = True
        flashes += 1

        for nb in neighbours(grid, *pos):
            flashes += gain_energy(grid, nb, flashed_pos)

    return flashes


grid = {(x, y): int(num) for y, line in enumerate(sys.stdin)
        for x, num in enumerate(line.strip())}

steps = 100
total_flashes = 0
for _ in range(steps):
    flashed_pos = {}
    for pos in grid:
        total_flashes += gain_energy(grid, pos, flashed_pos)

# result
# sample: 1656
# puzzle: 1747
print(total_flashes)
