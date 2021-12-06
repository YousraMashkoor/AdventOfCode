
import sys
from collections import defaultdict, Counter

infile = 'input.txt'
X = Counter([int(x) for x in open(infile).read().strip().split(',')])


def solve(S, n):
    X = S
    for day in range(n):
        Y = defaultdict(int)

        for x,cnt in X.items():
            if x==0:
                Y[6] += cnt #new timer of current fishes
                Y[8] += cnt #new fishes borned
            else:
                Y[x-1] += cnt
        X = Y
    return sum(X.values())

print(solve(X, 80))
print(solve(X, 256))