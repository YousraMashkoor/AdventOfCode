count = 0
count2 = 0

num = [int(x) for x in open('input.txt').read().split()]

for n in range(1, len(num)):
    if num[n-1]<num[n]:
        count += 1
    if n > 2 and n+1 != 3 and sum([num[n],num[n-1],num[n-2]]) > sum([num[n-1],num[n-2],num[n-3]]):
        count2 += 1


    
print("part 1:", count)
print("part 2:", count2)


