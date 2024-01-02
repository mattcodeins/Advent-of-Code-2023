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

import z3

# BitVec is way faster than Int
I = lambda name: z3.Real(name)

x, y, z = I('x'), I('y'), I('z')
vx, vy, vz = I('vx'), I('vy'), I('vz')

s = z3.Solver()

for i, a in enumerate(hailstones):
	(ax, ay, az), (vax, vay, vaz) = a

	t = I(f't_{i}')
	s.add(t >= 0)
	s.add(x + vx * t == ax + vax * t)
	s.add(y + vy * t == ay + vay * t)
	s.add(z + vz * t == az + vaz * t)

assert s.check() == z3.sat

m = s.model()
x, y, z = m.eval(x), m.eval(y), m.eval(z)
x, y, z = x.as_long(), y.as_long(), z.as_long()

print(x, y, z)

print(x + y + z)