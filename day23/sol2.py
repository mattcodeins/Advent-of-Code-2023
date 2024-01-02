import copy

f = open('day23/input.txt')
f = open('day23/ex.txt')

grid = []
for line in f.readlines():
    row = []
    for c in line.strip('\n'):
        if c in '^v<>':
            row.append('.')
        else:
            row.append(c)
    grid.append(row)
f.close()
for row in grid:
    print(''.join(row))

graph = {}

def traverse(start):
    pos =  start
    dist = 1
    while True:
        x, y = pos
        if pos == (len(grid[0])-2, len(grid)-1) or pos in graph:
            # for row in grid:
            #     print(''.join(row))
            # print(dist)
            return pos, dist

        grid[y][x] = 'O'
        paths = []
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            i, j = x+di, y+dj
            if grid[j][i] == '.':
                paths.append((i,j))
        if len(paths) > 1:
            graph[start] = graph.get(start, []) + [(pos, dist)]
            for i, cont in enumerate(paths):
                end, dist = traverse(cont)
                graph.append((pos, paths))
            return dist
        else:
            pos = paths[0]
            dist += 1

print(traverse((1,0)))
