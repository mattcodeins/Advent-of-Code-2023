def solve(parts):
    def search_for_part(li, ri, row):
        if li == 0:
            li = 1
        if ri == len(parts[row])-1:
            ri = len(parts[row])-2
        if row > 0:
            for i in range(li-1, ri+2):
                if parts[row-1][i] and not isinstance(parts[row-1][i], int):
                    return True
        if row < len(parts)-1:
            for i in range(li-1, ri+2):
                if parts[row+1][i] and not isinstance(parts[row+1][i], int):
                    return True
        if parts[row][li-1] and not isinstance(parts[row][li-1], int):
            return True
        if parts[row][ri+1] and not isinstance(parts[row][ri+1], int):
            return True
        return False

    total = 0
    for row, partline in enumerate(parts):
        if row != 0 and search_for_part(li, i, row-1):
            total += num
        num = 0
        for i, part in enumerate(partline):
            if isinstance(part, int):
                if num == 0:
                    li = i
                num = num*10 + part
            elif num != 0:
                if search_for_part(li, i-1, row):
                    total += num
                num = 0
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
    #     print(p)
    print(total)