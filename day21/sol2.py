from collections import deque

f = open('day21/input.txt')
# f = open('day21/ex.txt')

garden = []
area = 0
for line in f.readlines():
    plots = []
    for c in line.strip("\n"):
        if c == 'S':
            start = (len(garden), len(plots))
            area += 1
        elif c == '.':
            area += 1
        plots.append(c)
    garden.append(plots)
print('g:', len(garden))

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
                    (not (x, y) in seen) and
                    garden[x % len(garden)][y % len(garden)] == '.'
                ):
                    if i % 2 == (steps+1) % 2:
                        total += 1
                    edge.append((x,y))
    return total

steps = int((len(garden)-1)/2)
print('(g+1)/2:', steps)
print(reachable_plots(garden, start, steps))
print(reachable_plots(garden, start, steps + len(garden)))
print(reachable_plots(garden, start, steps + 2*len(garden)))

# print('G:', area)

# steps = 26501365
# area = 3691

# q = steps/len(garden)
# r = steps%len(garden)
# print(q, r)
# print((len(garden)-1)/2)
# print(area*2*q*q)
# q = steps/len(garden)
# print(area*2*q*q)