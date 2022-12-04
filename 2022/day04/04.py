from collections import defaultdict, Counter

def day_04(file):
    p1 = 0
    p2 = 0
    for line in open(file):
        a, b = line.strip().split(',')

        a1, a2 = a.split('-')
        b1, b2 = b.split('-')
        a1 = int(a1)
        a2 = int(a2)
        b1 = int(b1)
        b2 = int(b2)
        
        # 2-8,3-7
        if (b1 >= a1 and b2 <= a2) or (a1 >= b1 and a2 <= b2):
            p1 += 1

        if (b1 >= a1 and b1 <= a2) or (a1 >= b1 and a1 <= b2):
            p2 += 1
    return p1, p2


for file in ['sample.txt','input.txt']:
    p1, p2 = day_04(file)

    # check if the test example passess
    if file == 'sample.txt':
        assert p1 == 2 #569 (worng)
        assert p2 == 4

    print(p1,p2)

'''
notes: 
1. forgot to convert string input to 
int, resulted in a wrong ans
2. again took time in reading input but
still relatively faster than before
'''