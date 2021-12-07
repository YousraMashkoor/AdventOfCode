import numpy as np

data = [int(x) for x in open('input.txt', 'r').read().split(',')]
pos = np.median(data)
print("pos:", pos)
# pos = 2

fuel = sum([abs(x-pos) for x in data])
print("part 01: ",fuel)



result = 100000000000
for pos in range(max(data)):
    fuel = 0
    for x in data:
        fuel += (abs(x-pos)**2+abs(x-pos))/2
        # fuel += abs(x-pos)*abs((x-pos)+1)/2
    if fuel < result:
        result = fuel

print("part 02: ",result)