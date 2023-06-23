from collections import defaultdict, Counter
import copy


def day_09(file):
    p1 = 0
    p2 = 0
    head = [0,0]
    tail = [0,0]
    ninth= [0,0]
    trail = []
    allowed = [1,-1,0]
    allowed2 = [0,1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]

    for line in open(file):
        cmd, steps = line.strip().split(' ')
        steps = int(steps)
        for steps in range(steps):
            # breakpoint()
            if cmd == 'U':
                head[1] += 1
                if head[0]-tail[0] not in allowed or head[1]-tail[1] not in allowed:
                    p1+=1
                    tail = copy.deepcopy(head)
                    tail[1] -=1 
                if head[0]-tail[0] not in allowed2 or head[1]-tail[1] not in allowed2:
                    p2+=1
                    ninth = copy.deepcopy(head)
                    ninth[1] -=1
            elif cmd == 'D':
                head[1] -= 1
                if head[0]-tail[0] not in allowed or head[1]-tail[1] not in allowed:
                    p1+=1
                    tail = copy.deepcopy(head)
                    tail[1] +=1
            elif cmd == 'R':
                head[0] += 1
                if head[0]-tail[0] not in allowed or head[1]-tail[1] not in allowed:
                    p1+=1
                    tail = copy.deepcopy(head)
                    tail[0] -=1
            elif cmd == 'L':
                head[0] -= 1
                if head[0]-tail[0] not in allowed or head[1]-tail[1] not in allowed:
                    p1+=1
                    tail = copy.deepcopy(head)
                    tail[0] +=1
            
            if tuple(tail) not in trail:
                trail.append(tuple(tail))

    # print(len(trail))

    return len(trail), p2


for file in ['sample2.txt','input.txt']:
    p1, p2 = day_09(file)

    # check if the test example passess
    # if file == 'sample.txt':
    #     assert p1 == 13
        # assert p2 == 26

    print(p1,p2)
