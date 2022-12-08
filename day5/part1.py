import sys
import re
print("Enter the data")


data = sys.stdin.read()   # Use Ctrl d to stop the input 

lines = [l for l in data.splitlines() if l.strip() != ""]

stack_lines = []
move_lines = []

for line in lines:
    if line.startswith("move"):
        move_lines.append(line)
    else:
        stack_lines.append(line)

print(stack_lines)

n_stacks = int([c for c in stack_lines[-1].split(" ") if c != ""][-1])

stacks = [[] for _ in range(n_stacks)]

for line_n, line in enumerate(stack_lines[::-1][1:]):
    for stack_n, index in enumerate(range(1, len(stack_lines[-2]), 4)):
        if line[index].strip() != "":
            stacks[stack_n].append(line[index])

print(stacks)

PART1_MODE = "p1"
PART2_MODE = "p2"

MODE = PART2_MODE

for line in move_lines:
    amount, from_, to = map(int, re.findall(r"move (?P<amount>\d+) from (?P<from_>\d+) to (?P<to>\d+)", line)[0])

    print(f"{amount=} {from_=} {to=}")
    print(stacks)

    from_stack_index = from_ - 1
    to_stack_index =   to    - 1

    if MODE == PART1_MODE:
        stacks[to_stack_index]    += stacks[from_stack_index][-amount:]
    stacks[from_stack_index]  =  stacks[from_stack_index][:-amount]
    print(stacks)

    print()
    print()


answer = ''.join([s[-1] for s in stacks])

print(f"Answer: {answer}")
