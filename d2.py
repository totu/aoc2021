#!/usr/bin/env python3

data = []
with open("2.in", "r") as _input:
    data = [x.strip() for x in _input.readlines()]

x = 0
y = 0

for d in data:
    direction, amount = d.split(" ")
    amount = int(amount)
    if direction in ["up", "backward"]:
        amount = amount * -1

    if direction in ["up", "down"]:
        x += amount
    else:
        y += amount


print(x, y, x*y)

