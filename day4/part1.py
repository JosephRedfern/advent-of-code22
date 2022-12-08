import sys
print("Enter the data")


data = sys.stdin.read()   # Use Ctrl d to stop the input 

def get_overlap(a1, a2):
    f = max(a1[0], a2[0])
    t = min(a1[1], a2[1])

    print(f"f: {f}")
    print(f"t: {t}")

    overlap = (t - f) + 1

    print(f"Overlap: {overlap}")

    return overlap


def fully_contains(a1, a2):
    return get_overlap(a1, a2) in (a1[1]-a1[0] + 1, a2[1]-a2[0] + 1)

score = 0
for n, line in enumerate(data.splitlines()):
    print(line)
    first, second = line.split(",")
    a1 = list(map(int, first.split("-")))
    a2 = list(map(int, second.split("-")))

    if get_overlap(a1, a2) > 0:
        print(f"yes, {line}")
        score += 1

    print()


print(f"Score: {score}")
