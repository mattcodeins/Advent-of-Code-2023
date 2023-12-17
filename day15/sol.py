f = open('day15/input.txt')
for line in f.readlines():
    input = line.strip("\n").split(",")

example = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(",")

def label_to_hash(label):
    code = 0
    for c in label:
        code += ord(c)
        code = (code*17) % 256
    return code

# total = 0
# for step in input:
#     total += label_to_hash(step)
# print(total)

boxes = []
for i in range(256):
    boxes.append([[],[]])

for step in input:
    if "-" in step:
        label = step.strip("-")
        box = label_to_hash(label)
        if label in boxes[box][0]:
            pos = boxes[box][0].index(label)
            boxes[box][0].pop(pos)
            boxes[box][1].pop(pos)
    else:
        label, focus = step.split("=")
        box = label_to_hash(label)
        if label in boxes[box][0]:
            pos = boxes[box][0].index(label)
            boxes[box][1][pos] = focus
        else:
            boxes[box][0].append(label)
            boxes[box][1].append(focus)
    
    # for i, b in enumerate(boxes):
    #     if b[0]:
    #         print(i, b)
    # print("\n")

power = 0        
for i, b in enumerate(boxes):
    for j, focus in enumerate(b[1]):
        power += (i+1)*(j+1)*int(focus)
print(power)
