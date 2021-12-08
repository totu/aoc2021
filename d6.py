#!/usr/bin/env python3

data = []
with open("6.in", "r") as _input:
    data = [int(x) for x in [x.strip().split(",") for x in _input.readlines()][0]]

fishes = set()

class Fish():
    def __init__(self, day=8):
        self.day = day

    def cycle(self):
        day = self.day
        if day == 0:
            new_fish = Fish()
            fishes.add(new_fish)
            day = 6
        else:
            day -= 1
        self.day = day

    def __str__(self):
        return str(self.day)

    def __repr__(self):
        return str(self.day)

for fish in data:
    fishes.add(Fish(int(fish)))

def cycle():
    tmp_fishes = fishes.copy()
    for fish in tmp_fishes:
        fish.cycle()

for _ in range(80):
    cycle()

print(len(fishes))
