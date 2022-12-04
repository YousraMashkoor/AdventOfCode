G = []
for line in open('sample.txt'):
    G.append([int(x) for x in list(line.strip())])
import pdb; pdb.set_trace()
R = len(G) # rows
C = len(G[0]) # cols

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678

DR = [-1,0,1,0]
DC = [0,1,0,-1]
ans = 0
for r in range(R):
    for c in range(C):
        ok = True
        for d in range(4): # 4 directions
            rr = r+DR[d] # 0-1=-1 
            cc = c+DC[d] # 0+0=0
            if 0<=rr<R and 0<=cc<C and G[rr][cc]<=G[r][c]: # adjacent elemets shouldbe smaller then the current element
                ok = False
        if ok:
            ans += G[r][c]+1
print("Part01", ans)
