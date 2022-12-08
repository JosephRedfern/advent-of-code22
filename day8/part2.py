import sys
import numpy as np

print("Enter the data")

data = [
    l for l in sys.stdin.read().splitlines() if len(l.strip()) > 0
]  # Use Ctrl d to stop the input

height_map = np.zeros((len(data), len(data[0])))

for row_n, row in enumerate(data):
    for col_n, item in enumerate(row):
        height_map[row_n, col_n] = int(item)



def scenic_score(row, col, height_map):
    our_height = height_map[row, col]

    above = height_map[:row, col][::-1]
    below = height_map[row + 1 :, col]
    left = height_map[row, :col][::-1]
    right = height_map[row, col + 1 :]

    running_score = 1
    line_score = 0
    for direction, line in zip(("left", "right", "above", "below"), (left, right, above, below)):
        for tree in line:
            line_score += 1
            if our_height <= tree:
                break
        line_score = max(1, line_score)
        running_score *= line_score
        line_score = 0
    return running_score
    

max_score = 0
for row_n, row in enumerate(data):
    for col_n, item in enumerate(row):
        if row_n > 0 and row_n < len(row)-1 and col_n > 0 and col_n < len(data) -1:
            s = scenic_score(row_n, col_n, height_map)
            if s > max_score:
                max_score = s

print(f"{max_score=}")
