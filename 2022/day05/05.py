from collections import defaultdict, Counter
import copy

def day_05(file, data):
    p1 = 0
    p2 = 0

    data2 = copy.deepcopy(data)
    
    for line in open(file):
        x = line.strip().split(' ')
        stacks = int(x[1])
        org = int(x[3])
        dest = int(x[-1])
        
        # part1
        data[dest-1].extend(data[org-1][:-(stacks+1):-1])
        data[org-1] = data[org-1][:-stacks:]
        
        # part2
        data2[dest-1].extend(data2[org-1][-stacks:])
        data2[org-1] = data2[org-1][:-stacks:]

    p1 =''
    for l in data:
        if len(l)>=1:
            p1 = p1 + l[-1]
        
    p2 =''
    for l in data2:
        if len(l)>=1:
            p2 = p2 + l[-1]
    
    return p1, p2


data1 = [['Z','N'],['M','C','D'],['P']]
data2 = [['B','S','V','Z','G','P','W'], ['J','V','B','C','Z','F'],['V','L','M','H','N','Z','D','C'],
            ['L','D','M','Z','P','F','J','B'],['V','F','C','G','J','B','Q','H'],['G','F','Q','T','S','L','B'],
            ['L','G','C','Z','V'],['N','L','G'],['J','F','H','C']]

for file, data in [('modified_sample.txt', data1),('modified_input.txt', data2)]:
    p1, p2 = day_05(file, data)

    # check if the test example passess
    # if file == 'sample.txt':
        # assert p1 == 2
        # assert p2 == 4

    print(p1,p2)

'''
notes:
1. manually created the list of stacks from input, this took 
time. But probably coming up with a logic would have taken more time?
2. Took alooooot of time figuring out how "reverse slicing" work. It was
more of a hit and trial. Need ot revice these concepts.
3. Got stuck with "shallow" and "deepcopy". -_-
Eventually had to import the copy module. Need to remmeber these stuffs
'''