from collections import defaultdict

gama = ''
elipson = ''
data = []
for line in open('input.txt').readlines():
    data.append(line.strip())

num = data
digits = len(num[0])

for i in range(digits):
    ones = 0
    zeroes = 0
    for x in num:
        if x[i] == '1':
            ones += 1
        else:
            zeroes += 1

    gama += ('1' if ones > zeroes else '0')
    elipson += ('0' if ones > zeroes else '1')

gama = int(gama, 2)
elipson = int(elipson, 2)

print("part 1:", gama * elipson)


# PART 02

o2 = None
co2 = None
comp = {'1': '0', '0': '1'}

for i in range(len(num)):
    ones = 0
    zeroes = 0

    if len(num) == 1:
        o2 = num[0]
        break
    for x in num:
        if x[i] == '1':
            ones += 1
        else:
            zeroes += 1

    if ones < zeroes:
        num = [x for x in num if x[i]=='0']
    else:
        num = [x for x in num if x[i]=='1']


num = data
for i in range(len(num)):
    # import pdb; pdb.set_trace()
    ones = 0
    zeroes = 0

    if len(num) == 1:
        co2 = num[0]
        break
    for x in num:
        if x[i] == '1':
            ones += 1
        else:
            zeroes += 1

    if ones < zeroes:
        num = [x for x in num if x[i]=='1']
    else:
        num = [x for x in num if x[i]=='0']


print("part 2:", int(o2,2) * int(co2,2))