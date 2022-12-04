count = 0
for line in open('input.txt'):
    _,ot =  line.strip().split('|')
    ot = ot.split()
    for val in ot:
        if len(val) in [2,4,3,7]:
            count +=1
print("part 01: ", count)