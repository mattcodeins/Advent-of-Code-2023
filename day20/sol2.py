from collections import deque
from math import prod

from regex import P

f = open('day20/input.txt')
# f = open('day20/ex.txt')

class FlipFlop:
    def __init__(self, outputs):
        self.on = False
        self.outputs = outputs

    def process(self, pulse):
        _, inp, freq = pulse
        if freq == 1:
            return []
        self.on = not self.on
        return [(inp,  out, int(self.on)) for out in self.outputs]

class Conjuction:
    def __init__(self, outputs):
        self.inputs = {}
        self.outputs = outputs

    def process(self, pulse):
        prevout, inp, freq = pulse
        self.inputs[prevout] = freq
        for freq in self.inputs.values():
            if freq == 0:
                return [(inp, out, 1) for out in self.outputs]
        return [(inp, out, 0) for out in self.outputs]

broadcasts = []
modules = {}
backmap = {}
for line in f.readlines():
    input, output = line.strip("\n").split(" -> ")
    output = output.split(", ") if ',' in output else [output]
    if input == "broadcaster":
        for out in output:
            broadcasts.append((input, out, 0))
        continue
    op, name = input[0], input[1:]
    for out in output:
        backmap[out] = backmap.get(out, set()).union({name})
    if op == '%':
        modules[name] = FlipFlop(output)
    else:
        modules[name] = Conjuction(output)

for out, inputs in backmap.items():
    if out not in modules:
        continue
    if type(modules[out]) == Conjuction:
        modules[out].inputs = {inp: 0 for inp in inputs}
# for k,v in modules.items():
#     print(k, v.__dict__)

freqs = [0,0]
i = 0
foundrx = False
states = []
while i < 1000000:
    pulses = deque(broadcasts)
    freqs[0] += len(pulses)+1
    while len(pulses) > 0:
        prevout, inp, freq = pulses.popleft()
        mod = modules.get(inp, None)
        if mod is None:
            continue
        out = modules[inp].process((prevout, inp, freq))
        if inp == 'cl':
            for k,v in mod.inputs:
                if v == 1:
                    print(k, i)
        for _, _, freq in out:
            freqs[freq] += 1
        # print(out)
        pulses.extend(out)
    i += 1
    if foundrx:
        break
    # state = []
    # for name, module in modules.items():
    #     if type(module) == FlipFlop:
    #         state.append(module.on)
    #     elif type(module) == Conjuction:
    #         for inp in module.inputs.values():
    #             state.append(inp)
    # if state in states:
    #     break
    # states.append(state)

# print(states)
print((freqs))