f = open('day19/input.txt')
# f = open('day19/ex.txt')

workflows = {}
firstparse = True
for line in f.readlines():
    if line == "\n":
        firstparse = False
        continue
    if firstparse:
        k, v = line.strip("\n}").split("{")
        instructs = v.split(",")
        workflows[k] = instructs

def parse_condition(instruct):
    if ":" not in instruct:
        return instruct, None, None, None
    condition, key = instruct.split(":")
    if "<" in condition:
        cat, num = condition.split("<")
        return key, cat, '<', int(num)
    else:
        cat, num = condition.split(">")
        return key, cat, '>', int(num)

def flow(part, key='in'):
    if key == 'A':
        accepted_parts.append(part)
        return
    if key == 'R':
        return

    for instruct in workflows[key]:
        key, cat, cond, num = parse_condition(instruct)
        if cat is None:
            flow(part, key)
        else:
            l, u = part[cat]
            if cond == '<':
                if u <= num:
                    return flow(part, key)
                elif l >= num:
                    continue
                else:
                    part2 = {}
                    for k, v in part.items():
                        part2[k] = v
                    part2[cat] = (l, num)
                    flow(part2, key)
                    part[cat] = (num, u)
            elif cond == '>':
                if l > num:
                    return flow(part, key)
                elif u < num:
                    continue
                else:
                    part2 = {}
                    for k, v in part.items():
                        part2[k] = v
                    part2[cat] = (num+1, u)
                    flow(part2, key)
                    part[cat] = (l, num+1)

accepted_parts = []
part = {}
for cat in 'xmas':
    part[cat] = (1,4001)

flow(part)

total = 0
for part in accepted_parts:
    ptotal = 1
    for v in part.values():
        ptotal *= (v[1]-v[0])
    total += ptotal
print(total)