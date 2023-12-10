f = open('day9/input.txt')
data = []
for line in f.readlines():
    l = []
    nums = line.strip("\n").split(" ")
    for n in nums:
        l.append(int(n))
    data.append(l)

def between(lst):
    if all([l == 0 for l in lst]):
        return 0
    res = []
    for i in range(len(lst)-1):
        res.append(lst[i+1]-lst[i])
    n = between(res)
    return lst[0] - n

# example = [10,13,16,21,30,45]
# print(between(example))

total = 0
for d in data:
    total += between(d)
print(total)