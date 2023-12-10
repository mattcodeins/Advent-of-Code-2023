def find_min(line):
    _, line = line.split(": ")
    draws = line.split("; ")
    mins = [0, 0 , 0]
    for d in draws:
        cubes = d.split(", ")
        for c in cubes:
            x = c.split(" ")
            n = int(x[0])
            colour = x[1][0]
            if colour == "r":
                mins[0] = max(mins[0], n)
            elif colour == "g":
                mins[1] = max(mins[1], n)
            elif colour == "b":
                mins[2] = max(mins[2], n)
    return mins[0]*mins[1]*mins[2]

def solve():
    f = open('day2/bags.txt')
    total = 0
    for i, line in enumerate(f.readlines()):
        total += find_min(line)
    print(total)

if __name__ == "__main__":
    solve()