#!/usr/bin/env python3

data = []
with open("3.in", "r") as _input:
    data = [x.strip() for x in _input.readlines()]


def analyze(data):
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
    return bits

bits = analyze(data)
most_common_bits = [bits[b]['common'] for b in bits]
filtered = [d for d in data if int(d[0]) == most_common_bits[0]]

#Oxygen
for i in range(0, len(data[0])+1):
    filtered = [f for f in filtered if int(f[i]) == most_common_bits[i]]
    if len(filtered) == 1:
        break
    bits = analyze(filtered)
    most_common_bits = [bits[b]['common'] for b in bits]

oxygen = filtered[0]

most_least_bits = [bits[b]['least'] for b in bits]
filtered = [d for d in data if int(d[0]) == most_least_bits[0]]

#CO2
for i in range(0, len(data[0])+1):
    filtered = [f for f in filtered if int(f[i]) == most_least_bits[i]]
    if len(filtered) == 1:
        break
    bits = analyze(filtered)
    most_least_bits = [bits[b]['least'] for b in bits]

co2 = filtered[0]

oxygen_rate = int("".join(map(str,oxygen)), 2)
co2_rate = int("".join(map(str,co2)), 2)
life_support_rating = oxygen_rate * co2_rate

print(life_support_rating)

