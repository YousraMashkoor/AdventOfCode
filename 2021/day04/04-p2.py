filee = 'input.txt'

inp = [int(x) for x in open(filee, 'r').readline().strip().split(',')]
bingo = []
board = []
board_found = False


for line in open(filee):
    line = line.strip().split()
    if not board_found:
        board_found = True
        continue
    if line:
        board.append([int(x) for x in line])
    else:
        if board:
            bingo.append(board)
            board = []

# ouff! finally the board is ready atleast TT
found = False
board = None
value = None
to_del = []
for val in inp:
    if not found:
        breaker = False
        for bi, b in enumerate(bingo):
            for ri, row in enumerate(b):
                for pi, pos in enumerate(row):
                    # if val == 13 and ri == 1 and pi == 2:
                    #     import pdb; pdb.set_trace()
                    #     print(bi)
                    if bingo[bi][ri][pi] == val:
                        bingo[bi][ri][pi] = 'X'
                        if all(ele == 'X' for ele in bingo[bi][ri]):
                            if len(bingo) == 1:
                                board = b
                                value = val
                                found = True
                                breaker = True
                            to_del.append(bi)
                            # break out of all 3 loops only if this condition is true
                            break
                        elif all(ele[pi] == 'X' for ele in bingo[bi]):
                            if len(bingo) == 1:
                                board = b
                                value = val
                                found = True
                                breaker = True
                            to_del.append(bi)
                            # breaker = True
                            break
                if breaker:
                    break
            if breaker:
                break
        if to_del:
            for index in sorted(to_del, reverse=True):
                del bingo[index]
            to_del = []

score = sum([val for row in board for val in row if val != 'X'])
print("part 02: ", score * value)

            
            
    
