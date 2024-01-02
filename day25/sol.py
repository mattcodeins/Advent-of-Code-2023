f = open('day25/input.txt')
# f = open('day25/ex.txt')

graph  = {}
for line in f.readlines():
    key, connections = line.strip('\n').split(': ')
    connections = connections.split(' ')
    if key not in graph:
        graph[key] = set()
    for c in connections:
        if c not in graph:
            graph[c] = set()
        graph[key].add(c)
        graph[c].add(key)

done = False
set1, set2 = set(graph.keys()), set()
while True:
    crosses = 0
    done = len(set2) > 0
    for k in set2:
        crosses += len(set1.intersection(graph[k]))
        if crosses > 3:
            done = False
            break
    if done:
        break
    badkey = max(set1, key=lambda x: len(graph[x].intersection(set2)))
    set1.remove(badkey)
    set2.add(badkey)

print(len(set1)*len(set2))