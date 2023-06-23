from collections import defaultdict, Counter
import copy



# for line in open(filee):
#     line = line.strip().split()
#     if not board_found:
#         board_found = True
#         continue
#     if line:
#         board.append([int(x) for x in line])
#     else:
#         if board:
#             bingo.append(board)
#             board = []


def day_08(file):
    p1 = 0
    p2 = 0

    grid= []

    top = 0
    right = 0
    left = 0
    bottom = 0

    for line in open(file):
        
        trees = [int(x) for x in line.strip().split(' ')]
        grid.append(trees)

    print(grid)

    for i, line in enumerate(grid):
        for j, tree in enumerate(line):
            if i in [0, len(grid)-1]:
                p1+=1
            
            
            
            if tree<top:
                top = tree
            elif tree<bottom:
                bottom = tree
            elif tree < right:
                right = tree
            elif tree < left:
                left = tree

    
    return p1, p2


for file in ['sample.txt']:
    p1, p2 = day_08(file)

    # check if the test example passess
    if file == 'sample.txt':
        assert p1 == 21
        # assert p2 == 26

    print(p1,p2)
