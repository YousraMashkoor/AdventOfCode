filee = 'input.txt'

inp = [ int(x) for x in open(filee, 'r').readline().strip().split(',')]
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
for val in inp:
    if not found:
        for bi, b in enumerate(bingo):
            for ri, row in enumerate(b):
                for pi, pos in enumerate(row):
                    if bingo[bi][ri][pi] == val:
                        bingo[bi][ri][pi] = 'X'
                        if all(ele == 'X' for ele in bingo[bi][ri]):
                            board = b
                            value = val
                            found = True
                        elif all(ele[pi] == 'X' for ele in bingo[bi]):
                            board = b
                            value = val
                            found = True

score = sum([val for row in board for val in row if val != 'X'])
print("part 01: ", score * value)

            
            
    
