import numpy as np


segment = []
result = []
result2 = []

for line in open('input.txt'):
    line = line.strip()
    x = line.replace(' -> ', ',').split(',')
    assert len(x) == 4
    segment.append([int(z) for z in x])

max = np.max(segment)
result.extend([[0 for _ in range(0,max+1)] for _ in range(0,max+1)])
result2.extend([[0 for _ in range(0,max+1)] for _ in range(0,max+1)])

## PART 01
for x in segment:
    
    if not (x[0] == x[2] or x[1] == x[3]):
        continue
    else:
        idx, fdx = sorted([x[0],x[2]])
        idy, fdy = sorted([x[1],x[3]])
        
        result[fdy][fdx] += 1
        while idx < fdx or idy < fdy:
            
            if idx != fdx:
                result[idy][idx] += 1
                idx +=1
            elif idy != fdy:
                result[idy][idx] += 1
                idy +=1
            else:
                continue         
count = sum([1 for x in result for i in x if i > 1])
print("part 1: ", count)


## PART 02
for x in segment:
    # import pdb; pdb.set_trace()

    if not (x[0] == x[2] or x[1] == x[3] or abs(x[0]-x[2]) == abs(x[1]-x[3])):
        continue
    else:
        idx, fdx = [x[0],x[2]]
        idy, fdy = [x[1],x[3]]
        
        result2[fdy][fdx] += 1 #9.5
        while idx != fdx or idy != fdy:
            
            if idx != fdx:
                result2[idy][idx] += 1
                idx +=(1 if idx < fdx else -1)
                if idy != fdy:
                    idy +=(1 if idy < fdy else -1)
            elif idy != fdy:
                result2[idy][idx] += 1
                idy +=(1 if idy < fdy else -1)
            else:
                continue
    
count = sum([1 for x in result2 for i in x if i > 1])
print("part 2: ", count)