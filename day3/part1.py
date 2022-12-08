import sys
print("Enter the data")


priorities = {chr(x): x+1 - ord('a') for x in range(ord('a'), ord('z')+1)}
priorities = {chr(x): x+1 - ord('a') for x in range(ord('a'), ord('z')+1)}

priorities.update({chr(x): x+1 - ord('A') + 26 for x in range(ord('A'), ord('Z')+1)})

data = sys.stdin.read()   # Use Ctrl d to stop the input 

score = 0

PART1_MODE = "P1"
PART2_MODE = "P2"


MODE = PART2_MODE

groups = [None, None, None]

for n, line in enumerate(data.splitlines()):
    if MODE == PART1_MODE:
        n_items = len(line)

        compartment_1_items = line[:n_items//2]
        compartment_2_items = line[n_items//2:]

        common_items = set(compartment_1_items).intersection(compartment_2_items)
        
        for item in common_items:
            score += priorities[item]
    elif MODE == PART2_MODE:
        groups[n%3] = line

        if n > 0 and (n+1)%3 == 0:
            print(groups[0], groups[1], groups[2])
            common_items = set(groups[0]).intersection(groups[1]).intersection(groups[2])
            print(common_items)
            for item in common_items:
                score += priorities[item]


print(f"Score: {score}")
