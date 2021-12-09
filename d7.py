#!/usr/bin/env python3

data = []
with open("7.in", "r") as _input:
    data = [int(x) for x in [x.strip().split(",") for x in _input.readlines()][0]]

least_movement = len(data)**9
answer = None
last = sorted(data)[-1]
for point in range(last+1):
    total = 0
    for position in data:
        distance = abs(position - point)
        distance = distance + sum(range(distance))
        total += distance
        if total > least_movement:
            break

    #print(total, position)
    if total < least_movement:
        least_movement = total
        answer = point

print(least_movement)
print(answer)
