import math

time = [59, 79, 65, 75]
distance = [597, 1234, 1032, 1328]

time = [7, 15, 30]
distance = [9, 40, 200]

def solve_quadratic(a,b,c):
    return (-b - (b**2 - 4*a*c)**0.5)/(2*a)

def find_times(t,d):
    tsmall = math.floor(solve_quadratic(1, -t, d))
    times = t - 2*tsmall-1
    return times

def remove_kerning(lst):
    tt = ""
    for t in lst:
        tt += str(t)
    return int(tt)

tt = remove_kerning(time)
dd = remove_kerning(distance)
print(tt)
print(dd)
print(find_times(tt,dd))

res = 1
for t,d in zip(time, distance):
    res*=find_times(t,d)
print(res)