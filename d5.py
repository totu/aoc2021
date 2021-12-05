#!/usr/bin/env python3

data = []
with open("5.in", "r") as _input:
    data = [x.strip().split(" -> ") for x in _input.readlines()]

# create world map
world = {}
flat = [i for sl in data for i in sl]
largest = 0
for f in flat:
    x, y = [x for x in map(int, f.split(","))]
    bigger = max(x, y) 
    if bigger > largest:
        largest = bigger

for i_x in range(largest+1):
    for i_y in range(largest+1):
        world[f"{i_x,i_y}"] = "."

# map in vents
for d in data:
    first = [int(x) for x in d[0].split(",")]
    second = [int(x) for x in d[1].split(",")]
    x_1 = min(first[1], second[1])
    y_1 = min(first[0], second[0])
    x_2 = max(first[1], second[1])
    y_2 = max(first[0], second[0])

    if y_1 == y_2:
        i_y = y_1
        for i_x in range(x_1, x_2+1):
            mark = world[f"{i_x,i_y}"]
            if mark == ".":
                world[f"{i_x,i_y}"] = 1
            else:
                world[f"{i_x,i_y}"] += 1
    elif x_1 == x_2:
        i_x = x_1
        for i_y in range(y_1, y_2+1):
            mark = world[f"{i_x,i_y}"]
            if mark == ".":
                world[f"{i_x,i_y}"] = 1
            else:
                world[f"{i_x,i_y}"] += 1


how_many_2s = 0
for ix in range(largest+1):
    for iy in range(largest+1):
        mark = world[f"{ix,iy}"]
        print(mark, end=" ")
        if isinstance(mark, int) and mark > 1:
            how_many_2s += 1
    print("")

print(f"\nanswer: {how_many_2s}")
