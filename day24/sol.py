f = open('day24/input.txt')
f = open('day24/ex.txt')

hailstones = []
for line in f.readlines():
    p, v = line.strip('\n').split(' @ ')
    pos = tuple(map(int, p.split(', ')))
    vel = tuple(map(int, v.split(', ')))
    hailstones.append((pos, vel))

print(hailstones)

def is_future(pos, h):
    u = pos[0] - h[0][0]
    v = pos[1] - h[0][1]
    if ((u >= 0 and h[1][0] >= 0 or u <= 0 and h[1][0] <= 0) and
        (v >= 0 and h[1][1] >= 0 or v <= 0 and h[1][1] <= 0)):
        return True

def intersection(h1, h2):
    x1, y1 = h1[0][0], h1[0][1]
    u1, v1 = h1[1][0], h1[1][1]
    x2, y2 = h2[0][0], h2[0][1]
    u2, v2 = h2[1][0], h2[1][1]
    if u1*v2 - u2*v1 == 0:
        return None
    y = (v1*v2*(x2-x1) + y1*u1*v2 - y2*u2*v1) / (u1*v2 - u2*v1)
    x = x2 + (y-y2)/v2 * u2
    pos = (x,y)
    for h in [h1, h2]:
        if not is_future(pos, h):
            return None
    return pos

test_area = (200000000000000, 400000000000000)
test_area = (7, 27)

total = 0
for i, h1 in enumerate(hailstones):
    for h2 in hailstones[i+1:]:
        pos = intersection(h1, h2)
        if pos == None:
            continue
        x,y = pos
        if x >= test_area[0] and x <= test_area[1] and y >= test_area[0] and y <= test_area[1]:
            print(pos)
            total += 1

print(total)