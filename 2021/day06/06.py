print("MY SOLUTION")

initial_fish = []

for line in open('input.txt'):
    initial_fish.extend([int(x) for x in line.split(',')])


for x in range(0, 256):
    new_fish = []
    for i,x in enumerate(initial_fish):
        if x == 0:
            initial_fish[i] = 6
            new_fish.append(8)
        else:
            initial_fish[i] = x-1
    initial_fish.extend(new_fish)

# print(initial_fish)
print(len(initial_fish))