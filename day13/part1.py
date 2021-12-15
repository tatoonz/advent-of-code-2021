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

direction, fold_line = instructions[0].replace('fold along ', '').split('=')
fold_line = int(fold_line)

result = set()
for x, y in dots:
    if direction == 'x':
        if x < fold_line:
            result.add((x, y))
        else:
            new_x = fold_line - (x - fold_line)
            result.add((new_x, y))
    else:
        if y < fold_line:
            result.add((x, y))
        else:
            new_y = fold_line - (y - fold_line)
            result.add((x, new_y))

# result:
# sample: 17
# puzzle: 618
print(len(result))
