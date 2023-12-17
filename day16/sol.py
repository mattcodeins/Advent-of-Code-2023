from collections import deque

def step(pos, direct):
    x, y = pos
    if direct == 0:
        return (x, y-1)
    if direct == 1:
        return (x+1, y)
    if direct == 2:
        return (x, y+1)
    if direct == 3:
        return (x-1, y)

def bfs(pos, direct, grid):
    seen = set()
    queue = deque()
    queue.append((pos, direct))
    while len(queue) > 0:
        pos, direct = queue.popleft()
        direct %= 4
        pos = step(pos, direct) 
        x, y = pos
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            continue
        if (pos, direct) in seen:
            continue
        seen.add((pos, direct))
        # print(pos, direct, grid[y][x])
        if (grid[y][x] == '\\' and direct % 2 == 0
            or grid[y][x] == '/' and direct % 2 == 1):
                queue.append((pos, direct-1))
        elif (grid[y][x] == '\\' and direct % 2 == 1
            or grid[y][x] == '/' and direct % 2 == 0):
                queue.append((pos, direct+1))
        elif (grid[y][x] == '|' and direct % 2 == 1
            or grid[y][x] == '-' and direct % 2 == 0):
                queue.append((pos, direct-1))
                queue.append((pos, direct+1))
        else:
            queue.append((pos, direct))

    allpos = set()
    for pos, _ in seen:
        # x, y = pos
        # grid[y][x] = '#'
        allpos.add(pos)
    return len(allpos)

f = open('day16/input.txt')
# f = open('day16/ex.txt')

grid = []
for line in f.readlines():
    grid.append([c for c in line.strip("\n")])

energized = []
# print('\n'.join([''.join(row) for row in grid]))
for i in range(len(grid)):
    count = bfs((i, -1), 2, grid)
    energized.append(count)
    count = bfs((i, len(grid[0])), 4, grid)
    # print('\n'.join([''.join(row) for row in grid]))
    energized.append(count)
for j in range(len(grid[0])):
    count = bfs((-1, j), 1, grid)
    energized.append(count)
    count = bfs((len(grid), j), 3, grid)
    # print('\n'.join([''.join(row) for row in grid]))
    energized.append(count)

print(energized)
print(max(energized))