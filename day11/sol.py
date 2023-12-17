f = open('day11/input.txt')
# f = open('day11/example.txt')

space = []
for line in f.readlines():
    l = [c for c in line.strip()]
    space.append(l)

galaxies = []
is_row_empty = [True]*len(space)
is_col_empty = [True]*len(space[0])

for i in range(len(space)):
    for j in range(len(space[0])):
        if space[i][j] == '#':
            is_row_empty[i] = False
            is_col_empty[j] = False
            galaxies.append((i, j))

def find_shortest_path(start, end):
    si, sj = start
    ei, ej = end
    if si > ei:
        si, ei = ei, si
    if sj > ej:
        sj, ej = ej, sj
    path = ei - si + ej - sj
    path += sum(is_row_empty[si:ei])*(1000000-1)
    path += sum(is_col_empty[sj:ej])*(1000000-1)
    return path

total_path = 0
for i, g in enumerate(galaxies):
    for j in range(i+1, len(galaxies)):
        path = find_shortest_path(g, galaxies[j])
        # print(path)
        total_path += path

print(total_path)