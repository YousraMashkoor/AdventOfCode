from collections import defaultdict, Counter
import copy


# [{<dir name>: (<parent dir>,<file_size>)}]

def day_07(file):
    p1 = 0
    p2 = 0
    dirs = {}
    dir = ''
    parent = ''
    path = []
    file_total = 0

    for line in open(file):
        ## process all commands
        if line[0] == '$':
            #figuring out dir
            if 'cd' in line:
                if 'cd ..' not in line:
                    dir = line[5:]
                    path.append(dir)
                else:
                    path.pop()

            elif 'ls' in line:
                continue
            else:
                



        
    
    return p1, p2


for file in ['sample.txt','input.txt']:
    p1, p2 = day_07(file)

    # check if the test example passess
    if file == 'sample.txt':
        assert p1 == 11
        assert p2 == 26

    print(p1,p2)
