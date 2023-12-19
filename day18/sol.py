f = open('day18/input.txt')
# f = open('day18/ex.txt')

directs = []
direct_map = {0:'R', 1:'D', 2:'L', 3:'U'}
for line in f.readlines():
    direct, length, colour = line.strip("\n").split(" ")
    hexcode = colour[2:-1]
    direct = direct_map[int(hexcode[-1])]
    length = int(hexcode[:-1], 16)
    directs.append((direct, int(length)))
print(directs)

pos = (0,0)
area = 0
for d in directs:
    prev_pos = pos
    if d[0] == 'R':
        pos = (pos[0] + d[1], pos[1])
    if d[0] == 'D':
        pos = (pos[0], pos[1] + d[1])
    if d[0] == 'L':
        pos = (pos[0] - d[1], pos[1])
    if d[0] == 'U':
        pos = (pos[0], pos[1] - d[1])
    area += (prev_pos[0]-pos[0])*(prev_pos[1]+pos[1])+d[1]

print(area//2+1)