import sys
print("Enter the data")

data = sys.stdin.read()   # Use Ctrl d to stop the input 

groups = []
running = 0
for line in data.splitlines():
    if line != "":
        running += int(line)
    else:
        groups.append(running)
        running = 0
groups.append(running)

max_group = max(groups)
top = sum(sorted(groups)[-3:])

print(f"Max: {max_group}")
print(f"Top 3: {top}")
