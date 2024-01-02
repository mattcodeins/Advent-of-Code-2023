from collections import deque

f = open('day22/input.txt')
f = open('day22/ex.txt')

bricks = []
for line in f.readlines():
    s, e = line.strip("\n").split('~')
    brick = []
    for b in [s,e]:
        b = b.split(',')
        brick.append((int(b[0]), int(b[1]), int(b[2])))
    bricks.append(tuple(brick))

bricks.sort(key=lambda x: x[0][2])

for i, b in enumerate(bricks):
    under = False
    newbricks = sorted(bricks[:i], key=lambda x: x[1][2])
    for bu in reversed(newbricks):
        if (b[0][0] > bu[1][0] or b[1][0] < bu[0][0]
            or b[0][1] > bu[1][1] or b[1][1] < bu[0][1]):
            continue
        bricks[i] = (
            (b[0][0], b[0][1], bu[1][2] + 1),
            (b[1][0], b[1][1], bu[1][2] + 1 + b[1][2] - b[0][2])
        )
        under = True
        break
    if not under:
        bricks[i] = (
            (b[0][0], b[0][1], 1),
            (b[1][0], b[1][1], 1 + b[1][2] - b[0][2])
        )

supportedby = []
for _ in bricks:
    supportedby.append(set())
for i in range(len(bricks)-1, -1, -1):
    b = bricks[i]
    for j in range(i-1, -1, -1):
        bu = bricks[j]
        if bu[1][2]+1 != b[0][2]:
            continue
        if (b[0][0] > bu[1][0] or b[1][0] < bu[0][0]
            or b[0][1] > bu[1][1] or b[1][1] < bu[0][1]):
            continue
        supportedby[i].add(j)

supporting = set()
for s in supportedby:
    if len(s) == 1:
        supporting.add(next(iter(s)))

supports = []
for _ in bricks:
    supports.append(set())
for i in range(len(bricks)):
    b = bricks[i]
    for j in range(i+1,len(bricks)):
        ba = bricks[j]
        if b[1][2]+1 != ba[0][2]:
            continue
        if (b[0][0] > ba[1][0] or b[1][0] < ba[0][0]
            or b[0][1] > ba[1][1] or b[1][1] < ba[0][1]):
            continue
        supports[i].add(j)

print(supportedby)
print(supports)
total = 0
for b in supporting:
    x = {b}
    q = deque()
    for k in supports[b]:
        q.append(k)
    print(q)
    while q:
        bq = q.popleft()
        for ix in x:
            supportedby[bq].remove(ix)
        if len(supportedby[bq]) == 0:
            total += 1
            for xx in supports[bq]:
                q.append(xx)

print(total)