op = {
    'Z': 3,
    'A': 1,
    'B':2,
    'C': 3,

    'X': 1,
    'Y':2}

d = {'X': 'loose',
    'Y': 'draw',
    'Z': 'win'}


# part 1
X = [x.strip() for x in open('sample.txt')]
# X = [x.strip() for x in open('input.txt')]
score1 = 0
score2 = 0
for x in X:

    p1 = x[0]
    p2 = x[-1]
    if p1 == 'C' and p2 == 'X': #loose
        # part2
        score2 += 1
        score1  += op[p2]
        score1 += 6
    elif p1 == 'A' and p2 == 'Z':
        # part2
        score2 += (2 + 6)
        score1  += op[p2]
        score1 += 0
    else:
        score1  += op[p2]
        if op[p1] < op[p2]:
            score1  += 6
        elif op[p1] == op[p2]:
            score1  += 3

        #part2
        if p2 == 'Y': #draw
            score2 += (op[p1] + 3)
        elif p2 == 'Z': #win
            score2 += 6
            print(list(op.values())[list(op.keys()).index(p1)+1])
            score2 += list(op.values())[list(op.keys()).index(p1)+1]
        else: # loose
            score2 += list(op.values())[list(op.keys()).index(p1)-1]

print(score1)
print(score2)

## part 2 - wrong ans


'''
note:
1. took alot of time in reading the input
2. wasted time in coming up with a logic,
a simple dict of all possible senarios (3x3 = 9)
3. got stuck with the wrong logic in part 2
would have been faster
'''
