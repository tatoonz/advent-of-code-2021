import sys
from math import floor

open_chunks = ['(', '[', '{', '<']
close_chunks = [')', ']', '}', '>']

valid_chunks = {t: True for t in zip(open_chunks, close_chunks)}
open_to_close_chunk = {open: close for open,
                       close in zip(open_chunks, close_chunks)}
close_score = {close: index+1 for index, close in enumerate(close_chunks)}

scores = []
for line in sys.stdin:
    open_chunk_stack = []
    invalid_syntax = False

    for char in line.strip():
        if char in open_chunks:
            open_chunk_stack.append(char)
        elif char in close_chunks:
            last_open_chunk = open_chunk_stack.pop()
            if (last_open_chunk, char) not in valid_chunks:
                invalid_syntax = True
                break

    if not invalid_syntax and len(open_chunk_stack) != 0:
        total_score = 0

        for open in reversed(open_chunk_stack):
            close = open_to_close_chunk[open]
            total_score = (total_score * 5) + close_score[close]

        scores.append(total_score)

# result
# sample: 288957
# puzzle: 4330777059
result = sorted(scores)[floor(len(scores) / 2)]
print(result)
