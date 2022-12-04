import numpy as np

open_list = ["(","<","[","{"]
close_list = [")",">","]","}"]
points = [1,4,2,3]
error_list = [3,25137,57,1197]
data = []

error = 0
for line in open('input.txt'):
    line = line.strip()
    stack = []
    flag = False
    for i in line:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                flag = True
                error += error_list[pos]
                break
    if flag == False:
        data.extend([line])
print("part 01: ", error)


weight = []
for line in data:
    line = line.strip()
    stack = []
    for i in line:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
    p=0
    stack.reverse()
    for x in stack:
        p *= 5
        i = open_list.index(x)
        p +=points[i]
    weight.append(p)

print("part 02: ", int(np.median(weight)))
