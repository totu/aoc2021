#!/usr/bin/env python3

data = []
with open("1.in", "r") as _input:
    data = [int(x) for x in _input.readlines()]

inc = 0
prev = sum(data[0:3])
for i in range(len(data)):
    d = sum(data[i:i+3])
    if d > prev:
        inc += 1
    prev = d

print(inc)
