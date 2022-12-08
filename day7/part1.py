import sys
from typing import Optional
import re
import dataclasses
print("Enter the data")

data = sys.stdin.read()   # Use Ctrl d to stop the input 

answer = None

@dataclasses.dataclass
class Node:
    name: str
    size: Optional[int] = 0
    children: list["Node"] = dataclasses.field(default_factory=list)
    parent: Optional["Node"] = None

    def get_size(self):
        return sum([c.get_size() for c in self.children ]) + self.size

    def __repr__(self):
        return f"<Node {self.name=} {len(self.children)=} {self.get_size()=}>"

line_match = re.compile(r"(?P<level> *)-(?P<name>.+) \((?P<type>(file|dir))(, )?(size=(?P<size>\d+))?\)")

all_dirs = []
root = None
current_dir = None
current_level = 0
for line in data.splitlines():
    print(f"> {line}")
    if line.startswith("$ "):
        command = line.split(" ")[1:]
        print(f"{command=}")
        if command[0] == "cd":
            if command[1] == "/":
                print(f"cd to /")
                if root is None:
                    root = Node(name="/")
                current_dir = root
            elif command[1] == "..":
                print(f"cd to parent (from {current_dir} to {current_dir.parent}")
                current_dir = current_dir.parent
            else:
                prev = current_dir
                current_dir = next(d for d in current_dir.children if d.name == command[1])
                print(f"cd'ed from {prev} to {current_dir}")
    elif line.startswith("dir"):
        name = line.split(" ")[-1]
        if len([n for n in current_dir.children if n.name == name]) == 0:
            node = Node(name=name)
            print(f"adding dir {name}")
            node.parent = current_dir
            current_dir.children.append(node)
            all_dirs.append(node)
    else:
        size, name = line.split(" ")
        size = int(size)

        print(f"adding file {name} of size {size} to {current_dir}")
        current_dir.children.append(Node(name=name, size=size))

print(root.get_size())

PART1_MODE = "p1"
PART2_MODE = "p2"
MODE = PART2_MODE

if MODE == PART1_MODE:
    answer = sum([n.get_size() for n in all_dirs if n.get_size() < 100000])
else:
    total_space = 70000000
    space_needed = 30000000
    unused_space = total_space - root.get_size()

    need_to_delete = space_needed - unused_space
    if unused_space > need_to_delete:
        answer = 0
    
    answer = sorted([d for d in all_dirs if d.get_size() >= need_to_delete] , key=lambda x: x.get_size())[0].get_size()

print(f"Answer: {answer}")
