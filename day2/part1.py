import sys

hPos = 0
depth = 0

for line in sys.stdin:
    cmd = line.split()

    match cmd[0]:
        case 'forward':
            hPos += int(cmd[1])
        case 'down':
            depth += int(cmd[1])
        case 'up':
            depth -= int(cmd[1])

print(hPos*depth)
