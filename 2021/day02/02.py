# PART 1

depth = 0
horizontal = 0

for line in open('input.txt').readlines():
    action, qty = line.strip().split()
    if action == 'forward':
        horizontal += int(qty)
    elif action == 'down':
        depth += int(qty)
    elif action == 'up':
        depth -= int(qty)

print("part 01: ", depth * horizontal)


# PART 2

depth = 0
horizontal = 0
aim = 0

for line in open('input.txt').readlines():
    action, qty = line.strip().split()
    if action == 'forward':
        horizontal += int(qty)
        depth += aim * int(qty)
    elif action == 'down':
        aim += int(qty)
    elif action == 'up':
        aim -= int(qty)

print("part 02: ", depth * horizontal)
