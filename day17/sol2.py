import math

f = open('day17/input.txt')
f = open('day17/ex.txt')

graph = []
dist = []
for line in f.readlines():
    graph.append([int(c) for c in line.strip("\n")])
    dist.append([math.inf for _ in line.strip("\n")])

print(len(graph), len(graph[0]))



heat, path = a_star()
print(heat)
print(path)