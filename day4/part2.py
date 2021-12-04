import sys

numbers = sys.stdin.readline().strip().split(',')

# discard line after the draw numbers
sys.stdin.readline()

board_input = ''
for line in sys.stdin:
    board_input += line

boards = [[[(num, 0) for num in line.split()] for line in board.split('\n')]
          for board in board_input.strip().split('\n\n')]

bingo_max_board_size = 5
win_boards = {}
last_win_board = None
last_drawed_num = None

for drawed_num in numbers:
    for bid, board in enumerate(boards):
        if bid in win_boards:
            continue

        rows = [0] * bingo_max_board_size
        cols = [0] * bingo_max_board_size

        for y, row in enumerate(board):
            for x, col in enumerate(row):
                num, marked = col[0], col[1]

                if num == drawed_num:
                    marked = 1

                rows[y] += marked
                cols[x] += marked
                board[y][x] = (num, marked)

                if rows[y] == bingo_max_board_size or cols[x] == bingo_max_board_size:
                    win_boards[bid] = True
                    last_drawed_num = drawed_num

                    if len(win_boards) == len(boards):
                        last_win_board = bid
                        break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break

sum = 0
for row in boards[last_win_board]:
    for col in row:
        if col[1] == 0:
            sum += int(col[0])

# result
# sample: 1924
# puzzle: 2980
print(sum * int(last_drawed_num))
