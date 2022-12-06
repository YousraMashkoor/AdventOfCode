from collections import defaultdict, Counter
import copy

def day_01(file):
    p1 = 0
    p2 = 0

    for line in open(file):
        pass
    
    return p1, p2


for file in ['sample.txt','input.txt']:
    p1, p2 = day_01(file)

    # check if the test example passess
    if file == 'sample.txt':
        assert p1 == 11
        assert p2 == 26

    print(p1,p2)
