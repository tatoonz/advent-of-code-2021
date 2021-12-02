import sys

hPos = 0
depth = 0
aim = 0

for line in sys.stdin:
    cmd = line.split()

    match cmd[0]:
        case 'forward':
            hPos += int(cmd[1])
            depth += aim * int(cmd[1])
        case 'down':
            aim += int(cmd[1])
        case 'up':
            aim -= int(cmd[1])

print(hPos*depth)
