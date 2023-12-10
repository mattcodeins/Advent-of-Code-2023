import math

leftright = "LRRRLRRLRLLRLRRLRLRLLRRRLRLRRRLRRRLRLRLRRLRLRRRLRRLLRRLLLRRLRRLRRRLRLRRRLRRLRRRLRRRLRRLRLLRRRLRLRRLRLRLRRRLRRLLRRRLLRRLRLRRLRRRLLLRRRLLRLLRRLRRRLRLRLRRLLLRRRLLRRLLLRLRLRRLLRLLRRLLLRRLLRRRLRLRRRLRLLRRRLRRRLRLRLRRRLRLRRRLRRRLRRRLLRLRLRLRRLRLRRRLRLRLLRRLRRLRRLRRRLRRRLRLLRLLLRRLRLRRRR"

f = open('day8/input.txt')
directs = {}
for line in f.readlines():
    node, lrs = line.strip("\n").split(" = ")
    l, r = lrs[1:-1].split(", ")
    directs[node] = (l, r)

nodes = []
for node in directs:
    if node[-1] == "A":
        nodes.append(node)

lengths = []
for node in nodes:
    steps = 0
    found = False
    while not found:
        for c in leftright:
            if node[-1] == "Z":
                lengths.append(steps)
                found = True
                break
            steps += 1
            if c == "L":
                node = directs[node][0]
            else:
                node = directs[node][1]

print(math.lcm(*lengths))