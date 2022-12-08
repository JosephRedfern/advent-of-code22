import sys
import re
print("Enter the data")

data = sys.stdin.read()   # Use Ctrl d to stop the input 

answer = None

PART1_MODE = 4
PART2_MODE = 14

MODE = PART2_MODE

for n in range(MODE, len(data)):
    if len(set(data[n-MODE:n])) == MODE:
        answer = n
        break


print(f"Answer: {answer}")
