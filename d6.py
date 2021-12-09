#!/usr/bin/env python3

data = []
with open("6.in", "r") as _input:
    data = [int(x) for x in [x.strip().split(",") for x in _input.readlines()][0]]

fishes = [0,0,0,0,0,0,0,0,0]

for fish in data:
    fishes[fish] += 1

def cycle():
    breeding = fishes.pop(0)
    fishes.append(breeding)
    fishes[6] += breeding

for i in range(256):
    cycle()
print(sum(fishes))

