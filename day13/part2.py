import sys

dots = set()
instructions = list()
for line in sys.stdin:
    line = line.strip()

    if ',' in line:
        x, y = line.split(',')
        dots.add((int(x), int(y)))

    if 'fold' in line:
        instructions.append(line)


for instruction in instructions:
    temp_dots = set()

    direction, fold_line = instruction.replace('fold along ', '').split('=')
    fold_line = int(fold_line)

    for x, y in dots:
        if direction == 'x':
            if x < fold_line:
                temp_dots.add((x, y))
            else:
                new_x = fold_line - (x - fold_line)
                temp_dots.add((new_x, y))
        else:
            if y < fold_line:
                temp_dots.add((x, y))
            else:
                new_y = fold_line - (y - fold_line)
                temp_dots.add((x, new_y))

    dots = temp_dots

max_x = max([x for x, _ in dots])
max_y = max([y for _, y in dots])

for y in range(max_y+1):
    for x in range(max_x+1):
        print('x' if (x, y) in dots else '.', end='')
    print()

# result
# sample:
#
# xxxxx
# x...x
# x...x
# x...x
# xxxxx
#
# puzzle:
#
# .xx..x....xxx..xxxx.x..x.xxxx.x..x.x..x
# x..x.x....x..x.x....x.x..x....x.x..x..x
# x..x.x....x..x.xxx..xx...xxx..xx...x..x
# xxxx.x....xxx..x....x.x..x....x.x..x..x
# x..x.x....x.x..x....x.x..x....x.x..x..x
# x..x.xxxx.x..x.xxxx.x..x.x....x..x..xx.
