import sys

open_chunks = ['(', '[', '{', '<']
close_chunks = [')', ']', '}', '>']
valid_chunks = {t: True for t in zip(open_chunks, close_chunks)}

error_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

total_error_scores = 0
for line in sys.stdin:
    open_chunk_stack = []
    for char in line.strip():
        if char in open_chunks:
            open_chunk_stack.append(char)
        elif char in close_chunks:
            last_open_chunk = open_chunk_stack.pop()

            if (last_open_chunk, char) not in valid_chunks:
                total_error_scores += error_scores[char]
                break

# result
# sample: 26397
# puzzle: 387363
print(total_error_scores)
