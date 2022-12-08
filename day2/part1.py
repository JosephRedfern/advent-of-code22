import sys
print("Enter the data")

data = sys.stdin.read()   # Use Ctrl d to stop the input 

# true == you win, false == you lose, None == draw
outcome_lut = {
    ("A", "X"): None, # rock rock
    ("A", "Y"): True, # rock paper
    ("A", "Z"): False, # rock scissor
    ("B", "X"): False, # paper rock
    ("B", "Y"): None, # paper paper
    ("B", "Z"): True, # paper scissor 
    ("C", "X"): True, # scissor rock
    ("C", "Y"): False, # scissor paper
    ("C", "Z"): None # scissor scissor
} 


# X == lose, Y == draw, Z == win
fixed_outcome_lut = {
    ("A", "X"): "Z", # they played rock, you need to lose, so play scissor (Z)
    ("A", "Y"): "X", # they played rock, you need to draw, so play rock (X)
    ("A", "Z"): "Y", # they played rock, you need to win,  so play paper (Y)
    ("B", "X"): "X", # they played paper, you need to lose, so play rock (X)
    ("B", "Y"): "Y", # they player paper, you need to draw, so play paper (Y)
    ("B", "Z"): "Z", # they played paper, you need to win, so play scissor (Z)
    ("C", "X"): "Y", # they played scissor, you need to lose, so play paper (Y)
    ("C", "Y"): "Z", # they played scissor, you need to draw, so play scissor (Y)
    ("C", "Z"): "X", # they player scissor, you need to win, so play rock (X)
}


shape_point = {
        "X": 1,
        "A": 1,
        "Y": 2,
        "B": 2,
        "Z": 3,
        "C": 3
}

part2_map = {
        "X": False,
        "Y": None,
        "Z": True
}

outcome_points = {
        True: 6, # Win == 6
        False: 0, # Lose == 0
        None: 3 # Draw == 3
}

PART1_MODE = "P1"
PART2_MODE = "P2"

MODE = PART2_MODE

score = 0
for line in data.splitlines():
    first, second = line.split(" ")


    if MODE == PART1_MODE:
        theirs, ours = first, second

        lut = fixed_outcome_lut

        outcome = outcome_lut[(theirs, ours)] 
        score += outcome_points[outcome]
        score += shape_point[ours]

    elif MODE == PART2_MODE:
        theirs, outcome = first, second

        ours = fixed_outcome_lut[(theirs, outcome)]
        score += outcome_points[part2_map[outcome]]
        score += shape_point[ours]


print(f"Score: {score}")
