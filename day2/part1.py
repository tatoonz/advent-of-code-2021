import sys

hPos = 0
depth = 0

for line in sys.stdin:
    cmd = line.split()

    units = int(cmd[1])
    match cmd[0]:
        case 'forward':
            hPos += units
        case 'down':
            depth += units
        case 'up':
            depth -= units

print(hPos*depth)
