def solve(parts):
    def search_for_part(li, ri, row):
        if li == 0:
            li = 1
        if ri == len(parts[row])-1:
            ri = len(parts[row])-2
        if row > 0:
            for i in range(li-1, ri+2):
                if parts[row-1][i] == "*":
                    return (row-1, i)
        if row < len(parts)-1:
            for i in range(li-1, ri+2):
                if parts[row+1][i] == "*":
                    return (row+1, i)
        if parts[row][li-1] == "*":
            return (row, li-1)
        if parts[row][ri+1] == "*":
            return (row, ri+1)

    gear_store = {}
    for row, partline in enumerate(parts):
        num = 0
        for i, part in enumerate(partline):
            if isinstance(part, int):
                if num == 0:
                    li = i
                num = num*10 + part
                if i == len(partline)-1 or not isinstance(partline[i+1], int):
                    coords = search_for_part(li, i, row)
                    if coords:
                        gear_store[coords] = gear_store.get(coords, []) + [num]
                    num = 0
    print(gear_store)
    total = 0
    for v in gear_store.values():
        if len(v) == 2:
            total += v[0]*v[1]
    return total

if __name__ == "__main__":
    f = open('day3/input.txt', 'r')
    parts = []
    for line in [line.rstrip('\n') for line in f]:
        partline = []
        for c in line:
            if c.isdigit():
                partline.append(int(c))
            elif c != ".":
                partline.append(c)
            else:
                partline.append("")
        parts.append(partline)
    solve(parts)
    total = solve(parts)
    # for p in parts[0:3]:
    #     print(p
    print(total)