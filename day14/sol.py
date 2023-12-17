import copy
from tqdm import tqdm

f = open('day14/input.txt')
# f = open('day14/ex.txt')

platform = []
for line in f.readlines():
    platform.append([c for c in line.strip("\n")])


def tilt(platform, dir):
    new_platform = []
    for row in platform:
        new_platform.append(["." for i in range(len(row))])
    total = 0
    if dir == "north":
        for j in range(len(platform[0])):
            block = 0
            for i in range(len(platform)):
                if platform[i][j] == "O":
                    new_platform[block][j] = "O"
                    block += 1
                elif platform[i][j] == "#":
                    new_platform[i][j] = "#"
                    block = i+1
    elif dir == "west":
        for i in range(len(platform)):
            block = 0
            for j in range(len(platform[0])):
                if platform[i][j] == "O":
                    new_platform[i][block] = "O"
                    block += 1
                elif platform[i][j] == "#":
                    new_platform[i][j] = "#"
                    block = j+1
    elif dir == "south":
        for j in range(len(platform[0])):
            block = len(platform)-1
            for i in range(len(platform)-1, -1, -1):
                if platform[i][j] == "O":
                    new_platform[block][j] = "O"
                    block -= 1
                elif platform[i][j] == "#":
                    new_platform[i][j] = "#"
                    block = i-1
    elif dir == "east":
        for i in range(len(platform)):
            block = len(platform[0])-1
            for j in range(len(platform[0])-1, -1, -1):
                if platform[i][j] == "O":
                    new_platform[i][block] = "O"
                    block -= 1
                elif platform[i][j] == "#":
                    new_platform[i][j] = "#"
                    block = j-1
    # print("\n".join(["".join(row) for row in new_platform]) + "\n")
    return new_platform

def total_weight(platform):
    total = 0
    for j in range(len(platform[0])):
        for i in range(len(platform)):
            if platform[i][j] == "O":
                total += len(platform)-i
    return total

def cycle(platform):
    platform = tilt(platform, "north")
    platform = tilt(platform, "west")
    platform = tilt(platform, "south")
    platform = tilt(platform, "east")
    total = total_weight(platform)
    return platform, total

for i in tqdm(range(10000)):
    platform, total = cycle(platform)
    if i > 10000-100:
        print(i+1, total)

## CHECK NOTES.txt ON HOW I SOLVED THIS (i.e. very dodgy)