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

    x_1 = first[1]
    x_2 = second[1]

    y_1 = first[0]
    y_2 = second[0]


    def get_range(i_1, i_2):
        i_1 = int(i_1)
        i_2 = int(i_2)
        if i_1 < i_2:
            i_range = range(i_1, i_2+1)
        else:
            i_range = range(i_1, i_2-1, -1)
        return i_range

    x_range = get_range(x_1, x_2) 
    y_range = get_range(y_1, y_2) 
    print("X", x_range)
    print("y", y_range)

    if y_1 == y_2:
        i_y = y_1
        for i_x in x_range:
            mark = world[f"{i_x,i_y}"]
            if mark == ".":
                world[f"{i_x,i_y}"] = 1
            else:
                world[f"{i_x,i_y}"] += 1
    elif x_1 == x_2:
        i_x = x_1
        for i_y in y_range:
            mark = world[f"{i_x,i_y}"]
            if mark == ".":
                world[f"{i_x,i_y}"] = 1
            else:
                world[f"{i_x,i_y}"] += 1
    else:
        assert len(x_range) == len(y_range)
        for i in range(len(x_range)):
            i_x = x_range[i]
            i_y = y_range[i]
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
