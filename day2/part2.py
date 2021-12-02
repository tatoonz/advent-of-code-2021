import sys

hPos = 0
depth = 0
aim = 0

for line in sys.stdin:
    cmd = line.split()

    units = int(cmd[1])
    match cmd[0]:
        case 'forward':
            hPos += units
            depth += aim * units
        case 'down':
            aim += units
        case 'up':
            aim -= units

# result
# sample: 900
# puzzle: 1599311480
print(hPos*depth)
