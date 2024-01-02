from collections import deque
from re import L

f = open('day21/input.txt')
# f = open('day21/ex.txt')

garden = []
for line in f.readlines():
    plots = []
    for c in line.strip("\n"):
        if c == 'S':
            start = (len(garden), len(plots))
        plots.append(c)
    garden.append(plots)
# print(garden)

def reachable_plots(garden, start, steps):
    seen = set()
    edge = deque([start])
    total = (steps+1) % 2
    for i in range(steps):
        for _ in range(len(edge)):
            p = edge.popleft()
            seen.add(p)
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = p[0] + di, p[1] + dj
                if (
                    (x,y) not in seen and
                    x < len(garden) and x >= 0 and
                    y < len(garden[0]) and y >= 0 and
                    garden[x][y] == '.'
                ):
                    if i % 2 == (steps+1) % 2:
                        garden[x][y] = 'O'
                        total += 1
                    edge.append((x,y))
    return total

steps = int((len(garden)+1)/2)
steps = 65
print('steps', steps)
print(reachable_plots(garden, start, steps))