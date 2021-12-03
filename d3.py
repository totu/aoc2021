#!/usr/bin/env python3

data = []
with open("3.in", "r") as _input:
    data = [x.strip() for x in _input.readlines()]

bits = {}
for b in range(len(data[0])):
    count_0 = 0
    count_1 = 0
    for d in data:
        bit = d[b]
        bit = d[b]
        count_0 += bit.count('0')
        count_1 += bit.count('1')
    common = 0 if count_0 > count_1 else 1
    least = 0 if common == 1 else 1
    bits[str(b)] = {'common': common, 'least': least}

gamma_bits = [bits[b]['common'] for b in bits]
epsilon_bits = [bits[b]['least'] for b in bits]

print("gamma", gamma_bits)
print("epsilon", epsilon_bits)
gamma_rate = int("".join(map(str,gamma_bits)), 2)
epsilon_rate = int("".join(map(str,epsilon_bits)), 2)

power_consumption = gamma_rate * epsilon_rate
print(power_consumption)
