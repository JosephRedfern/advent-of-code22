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


def is_visible(row, col, height_map):
    return not all(
        [
            np.any(height_map[:row, col] >= height_map[row, col]),
            np.any(height_map[row + 1 :, col] >= height_map[row, col]),
            np.any(height_map[row, :col] >= height_map[row, col]),
            np.any(height_map[row, col + 1 :] >= height_map[row, col]),
        ]
    )


visible = 0
for row_n, row in enumerate(data):
    for col_n, item in enumerate(row):
        if row_n > 0 and row_n < len(row)-1 and col_n > 0 and col_n < len(data) -1:
            v = is_visible(row_n, col_n, height_map)
            if v:
                visible += 1
            print(f"{row_n=} {col_n=} {item=} {v=}")

edges = (2*len(data) + 2*len(data[0])) - 4 # corners shouldn't be counted twice
print(f"{edges=}")
print(edges+ visible)
