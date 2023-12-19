import math

f = open('day17/input.txt')
f = open('day17/ex.txt')

graph = []
dist = []
for line in f.readlines():
    graph.append([int(c) for c in line.strip("\n")])
    dist.append([math.inf for _ in line.strip("\n")])

print(len(graph), len(graph[0]))

def h(coords):
    return len(graph)-coords[0]+len(graph[0])-coords[1]-2

def a_star():
    open_set = {(0,0)}
    came_from = {}
    gdist = []
    fdist = []
    for _ in graph:
        _gdist = []
        _fdist = []
        for _ in graph[0]:
            _gdist.append(math.inf)
            _fdist.append(math.inf)
        gdist.append(_gdist)
        fdist.append(_fdist)
    gdist[0][0] = 0
    fdist[0][0] = h((0,0))

    while len(open_set) > 0:
        fcurr = math.inf
        for i, j in open_set:
            if fdist[i][j] < fcurr:
                ci, cj = i, j
                fcurr = fdist[i][j]

        if (ci, cj) == (len(graph)-1,len(graph[0])-1):
            return fcurr, find_path(came_from, (ci, cj))

        open_set.remove((ci, cj))
        neighbours = check_directs(came_from, (ci, cj))
        for ni, nj in neighbours:
            if ni < 0 or ni >= len(graph) or nj < 0 or nj >= len(graph[0]):
                continue
            t_gdist = gdist[ci][cj] + graph[ni][nj]
            if t_gdist < gdist[ni][nj]:
                came_from[(ni,nj)] = (ci,cj)
                gdist[ni][nj] = t_gdist
                fdist[ni][nj] = t_gdist + h((ni, nj))
                if (ni, nj) not in open_set:
                    open_set.add((ni, nj))

def find_path(came_from, curr, max_hist=-1):
    total_path = [curr]
    while curr in came_from:
        if len(total_path) == max_hist:
            return total_path
        curr = came_from[curr]
        total_path.append(curr)
    return total_path

def check_directs(came_from, curr):
    directs = [(1,0), (0,1), (-1,0), (0,-1)]
    neighbours = []
    for di, dj in directs:
        neighbours.append((curr[0]+di, curr[1]+dj))
    path = find_path(came_from, curr, 4)
    if len(path) > 1:
        last = path[1]
        to_last = (last[0] - curr[0], last[1] - curr[1])
        neighbours.pop(directs.index(to_last))
        directs.remove(to_last)
        if len(path) == 4:
            first = path[-1]
            if curr[0] - first[0] == 3:
                neighbours.pop(directs.index((1,0)))
                directs.remove((1,0))
            if first[0] - curr[0] == 3:
                neighbours.pop(directs.index((-1,0)))
                directs.remove((-1,0))
            if curr[1] - first[1] == 3:
                neighbours.pop(directs.index((0,1)))
                directs.remove((0,1))
            if first[1] - curr[1] == 3:
                neighbours.pop(directs.index((0,-1)))
                directs.remove((0,-1))
    return neighbours

heat, path = a_star()
print(heat)
print(path)