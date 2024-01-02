import copy
import sys
sys.setrecursionlimit(1500)

f = open('day23/input.txt')
# f = open('day23/ex.txt')

grid = []
for line in f.readlines():
    grid.append([c for c in line.strip('\n')])
f.close()

arrows = {'^':(0,-1), 'v':(0,1), '<':(-1,0), '>':(1,0)}

def traverse(pos, dist=0, grid=grid):
    paths = [pos]
    while len(paths) == 1:
        dist += 1
        pos = paths.pop()
        x, y = pos
        if pos == (len(grid[0])-2, len(grid)-1):
            # for row in grid:
            #     print(''.join(row))
            # print(dist)
            return dist-1

        if grid[y][x] in arrows:
            di, dj = arrows[grid[y][x]]
            grid[y][x] = 'O'
            paths = [(x+di, y+dj)]
            continue
        grid[y][x] = 'O'
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            i, j = x+di, y+dj
            if grid[j][i] == '.' or grid[j][i] in arrows:
                paths.append((i,j))
    dists = []
    grid = copy.deepcopy(grid)
    dist = copy.deepcopy(dist)
    for pos in paths:
        dists.append(traverse(pos, dist, grid))
    return max(dists) if dists else 0

# grid[len(grid)-2][1] = 'O'
print(traverse((1,0)))
