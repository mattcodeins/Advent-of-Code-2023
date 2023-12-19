f = open('day19/input.txt')
# f = open('day19/ex.txt')

workflows = {}
parts = []
firstparse = True
for line in f.readlines():
    if line == "\n":
        firstparse = False
        continue
    if firstparse:
        k, v = line.strip("\n}").split("{")
        instructs = v.split(",")
        workflows[k] = instructs
    else:
        vals = line.strip("{}\n").split(",")
        part = {}
        for v in vals:
            k, n = v.split("=")
            part[k] = int(n)
        parts.append(part)

def parse_condition(instruct, part):
    if ":" not in instruct:
        return instruct
    condition, key = instruct.split(":")
    if "<" in condition:
        cat, num = condition.split("<")
        if part[cat] < int(num):
            return key
    else:
        cat, num = condition.split(">")
        if part[cat] > int(num):
            return key

def sort_part(part, flowkey='in'):
    flow = workflows[flowkey]
    for instruct in flow:
        key = parse_condition(instruct, part)
        if key:
            break
    if key == 'A' or key == 'R':
        return key
    return sort_part(part, key)

total = 0
for part in parts:
    if sort_part(part) == 'A':
        total += sum(part.values())
print(total)