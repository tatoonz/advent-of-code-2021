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

    if grid[pos] > 9:
        grid[pos] = 0
        flashed_pos[pos] = True

        for nb in neighbours(grid, *pos):
            gain_energy(grid, nb, flashed_pos)


grid = {(x, y): int(num) for y, line in enumerate(sys.stdin)
        for x, num in enumerate(line.strip())}

step = 0
while True:
    step += 1
    flashed_pos = {}
    for pos in grid:
        gain_energy(grid, pos, flashed_pos)

    if len(flashed_pos) == len(grid):
        break

# result
# sample: 195
# puzzle: 505
print(step)
