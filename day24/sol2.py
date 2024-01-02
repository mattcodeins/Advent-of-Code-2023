import numpy as np
import random

f = open('day24/input.txt')
# f = open('day24/ex.txt')

hailstones = []
for line in f.readlines():
    p, v = line.strip('\n').split(' @ ')
    pos = tuple(map(int, p.split(', ')))
    vel = tuple(map(int, v.split(', ')))
    hailstones.append((pos, vel))

# print(hailstones)

for _ in range(1000000):
    A = []
    b = []
    zs = []
    ws = []
    idxs = []
    for _ in range(3):
        idxs.append(random.randint(0, len(hailstones)-1))
    for i in idxs:
        pos, vel = hailstones[i]
        x, y, z = pos
        u, v, w = vel
        A.append([-v, u, y, -x, 1, -1])
        b.append([y*u - x*v])
        zs.append(z)
        ws.append(w)
    A = np.array(A)
    sing = np.linalg.matrix_rank(A)
    if sing != 4:
        continue

    x = np.linalg.lstsq(A, b, rcond=None)[0]
    if abs(x[2] - int(x[2])) < 0.000001 and abs(x[3] - int(x[3])) < 0.000001:
        t1 = ((x[0] + A[0,3])/(A[0,1] - x[2]))
        t2 = ((x[0] + A[1,3])/(A[1,1] - x[2]))
        z1, z2 = zs[0], zs[1]
        w1, w2 = ws[0], ws[1]
        w = (z1-z2 + w1*t1 - w2*t2)/(t1-t2)
        if np.isnan(w):
            continue
        if abs(w - int(w)) < 0.000001:
            print(x[2:4], w)
            break

print('t1', t1)
print('t2', t2)


z = (t2*(z1 + w2*t1) - t1*(z2 + w1*t2))/(t2 - t1)
print(z)

ans = x[0] + x[1] + z
print('HERE')
print(ans)
