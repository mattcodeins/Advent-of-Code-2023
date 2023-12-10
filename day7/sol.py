import functools
import re

f = open('day7/input.txt')

res = []
for line in f.readlines():
    hand, bid = line.strip("\n").split(" ")
    cc = {}
    for c in hand:
       cc[c] = cc.get(c,0) + 1
    if "J" in cc.keys():
        print(cc)
        tmp = cc["J"]
        del cc["J"]
        if len(cc) > 0:
            topkey = max(cc, key=cc.get)
            cc[topkey] += tmp
        else:
            cc["A"] = 5
        print(cc)
    if len(cc) == 1:
        res.append((6, hand, bid))
    elif len(cc) == 2:
        for v in cc.values():
            if v == 4:
                res.append((5, hand, bid))
            elif v == 3:
                res.append((4, hand, bid))
    elif len(cc) == 3:
        for v in cc.values():
            if v == 2:
                res.append((2, hand, bid))
                break
            elif v == 3:
                res.append((3, hand, bid))
    elif len(cc) == 4:
        res.append((1, hand, bid))
    else:
        res.append((0, hand, bid))
print(len(res))

def card_to_score(card):
    if card == "A":
        return 14
    if card == "K":
        return 13
    if card == "Q":
        return 12
    if card == "J":
        return 1
    if card == "T":
        return 10
    return int(card)

def score(hand):
    return hand[0]*10000000000 + card_to_score(hand[1][0])*100000000 + card_to_score(hand[1][1])*1000000 + card_to_score(hand[1][2])*10000 + card_to_score(hand[1][3])*100 + card_to_score(hand[1][4])

res.sort(key=score)

total = 0
for i, v in enumerate(res):
    # print(v, i)
    total += int(v[2])*(i+1)
print(total)