REAL = True
# REAL = False

if REAL:
    f = open('day10/input.txt')
else:
    f = open('day10/example.txt')

grid = []
for i, line in enumerate(f.readlines()):
    line = line.strip("\n")
    pipes = []
    for j, c in enumerate(line):
        if c == "S":
            s = (i, j)
        pipes.append(c)
    grid.append(pipes)

def traverse(coord, prev):
    i, j = coord
    pipe = grid[i][j]
    if pipe == "|":
        if prev == (i-1, j):
            return (i+1, j), coord
        return (i-1, j), coord
    if pipe == "J":
        if prev == (i-1, j):
            return (i, j-1), coord
        return (i-1, j), coord
    if pipe == "L":
        if prev == (i-1, j):
            return (i, j+1), coord
        return (i-1, j), coord
    if pipe == "-":
        if prev == (i, j-1):
            return (i, j+1), coord
        return (i, j-1), coord
    if pipe == "F":
        if prev == (i, j+1):
            return (i+1, j), coord
        return (i, j+1), coord
    if pipe == "7":
        if prev == (i, j-1):
            return (i+1, j), coord
        return (i, j-1), coord

prev_up = s
prev_down = s
if REAL:
    up = (s[0]-1, s[1])
    down = (s[0]+1, s[1])
else:
    up = (s[0], s[1]+1)
    down = (s[0]+1, s[1])
steps = 1
border = set([prev_up, up, down])
while up != down:
    steps += 1
    up, prev_up = traverse(up, prev_up)
    down, prev_down = traverse(down, prev_down)
    border.add(up)
    border.add(down)

if REAL:
    grid[s[0]][s[1]] = "|"
else:
    grid[s[0]][s[1]] = "F"



total = 0
for i, line in enumerate(grid):
    inside = False
    prev = None
    for j, c in enumerate(line):
        pipe = grid[i][j]
        if (i, j) in border:
            if (
                pipe == "|" or
                (pipe == "7" and prev == "L") or
                (pipe == "J" and prev == "F")
                ):
                inside = not inside
            if pipe != "-":
                prev = pipe
        elif inside:
            total += 1
print(total)