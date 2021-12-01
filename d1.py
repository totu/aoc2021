#!/usr/bin/env python3

data = []
with open("1.in", "r") as _input:
    data = [int(x) for x in _input.readlines()]

inc = 0
prev = data[0]
for d in data:
    if d > prev:
        inc += 1
    prev = d

