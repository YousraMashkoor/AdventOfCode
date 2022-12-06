from collections import defaultdict, Counter
import copy

def day_06(file):
    p1 = 0
    p2 = 0

    chars = []
    chars2 = []

    for line in open(file):
        for i, c in enumerate(line):
            if len(chars)<4:
                chars.append(c)
            if len(set(chars)) == 4:
                p1 = i+1
                break
            elif len(chars)== 4 and len(set(chars)) != 4:
                chars.pop(0)

        for i, c in enumerate(line):
            if len(chars2)<14:
                chars2.append(c)

            if len(set(chars2)) == 14:
                p2 = i+1
                break
            elif len(chars2)== 14 and len(set(chars2)) != 14:
                chars2.pop(0)
        
    
    return p1, p2


for file in ['sample.txt','input.txt']:
    p1, p2 = day_06(file)

    # check if the test example passess
    if file == 'sample.txt':
        assert p1 == 11
        assert p2 == 26

    print(p1,p2)


'''
notes: took time understanding the prob, 
need to work on speed.
'''