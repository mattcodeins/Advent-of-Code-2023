f = open('day13/input.txt')
# f = open('day13/ex.txt')

patterns = []
grid = []
for line in f.readlines():
    if line != "\n":
        grid.append(list(line.strip("\n")))
    else:
        patterns.append(grid)
        grid = []

def find_mirror_line(lines, oldlineval):
    # print(lines, oldlineval)
    for mirroredge in range(len(lines)-1):
        l, r = mirroredge, mirroredge+1
        isedge = True
        while l >= 0 and r < len(lines):
            if lines[l] == lines[r]:
                l -= 1
                r += 1
            else:
                isedge = False
                break
        if isedge and mirroredge+1 != oldlineval:
            return mirroredge+1
    return 0

def search_all_lines(pattern, oldline=(-1, False)):
    rows = ["".join(row) for row in pattern]
    if oldline[1]:
        rowi = find_mirror_line(rows, oldline[0])
    else:
        rowi = find_mirror_line(rows, 0)
    if rowi:
        return (rowi, True)
    cols = ["".join(col) for col in zip(*pattern)]
    if not oldline[1]:
        coli = find_mirror_line(cols, oldline[0])
    else:
        coli = find_mirror_line(cols, 0)
    return (coli, False)

# print(patterns)
res = 0
for p in patterns:
    oldline = search_all_lines(p)
    print("oldline", oldline)
    found = False
    for i in range(len(p)):
        for j in range(len(p[0])):
            p[i][j] = "." if p[i][j] == "#" else "#"
            line = search_all_lines(p, oldline)
            if line[0]:
                found = True
                print("newline", line)
                break
            p[i][j] = "." if p[i][j] == "#" else "#" 
        if found:
            break
    val, isrow = line
    if isrow:
        res += val*100
    else:
        res += val
print(res)