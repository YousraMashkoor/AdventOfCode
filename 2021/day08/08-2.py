from collections import defaultdict

digits = defaultdict(int) # stores each wire link position 
#  dddd           1111
# e    a         2    3
# e    a         2    3
#  ffff  --->     4444
# g    b         5    6
# g    b         5    6
#  cccc           7777

new_keys = defaultdict(str)


def get_diff(a,b):
    a=set(a)
    b=set(b)
    return list(a-b)

def get_union(a,b):
    a=set(a)
    b=set(b)
    return list(a|b)

def matched(a,b):
    a=set(a)
    b=set(b)
    return a==b


result = 0
for line in open('input.txt'):
    inp, ot =  line.strip().split('|')
    ot = ot.split()
    inp = inp.split()
    
    pair_6digits = []
    pair_5digits = []

    for val in inp:
        if len(val) == 2:
            new_keys[1] = val
        elif len(val) == 7:
            new_keys[8] = val
        elif len(val) == 4:
            new_keys[4] = val
        elif len(val) == 3:
            new_keys[7] = val
        elif len(val) == 6:
            pair_6digits.append(val)
        elif len(val) == 5:
            pair_5digits.append(val)
    
    ## get new 'a'
    digits[1] = get_diff(new_keys[7], new_keys[1])
    ## get new 'g'
    for fiv in pair_5digits:
        x = get_diff(fiv, new_keys[4])
        if len(x) == 2:
            digits[7] = get_diff(x,digits[1])
    ## get new 'e'
    for fiv in pair_5digits:
        x = get_diff(fiv, new_keys[4])
        if len(x) == 3:
            digits[5] = get_diff(get_diff(x,digits[1]), digits[7])
    ## get new 0
    x = get_union(digits[1] + digits[7] + digits[5], new_keys[1])
    for val in pair_6digits:
        x2 = get_diff(val, x)
        if len(x2) == 1:
            new_keys[0] = val
            pair_6digits.remove(val)
            break
    ## get new 'd'
    digits[4] = get_diff(new_keys[8], new_keys[0])
    ## get new 3
    x = get_union(digits[1] + digits[7] + digits[4], new_keys[1])
    for val in pair_5digits:
        if matched(val, x):
            new_keys[3] = val
            pair_5digits.remove(val)

    ## get new 9
    for val in pair_6digits:
        x = get_diff(val, new_keys[3])
        if len(x) == 1:
            digits[2] = x
            new_keys[9] = val
            pair_6digits.remove(val)

    ## get new 6
    new_keys[6] = pair_6digits[0]
    
    ## get new 2
    for val in pair_5digits:
        if len(get_diff(new_keys[9], val)) == 2:
            new_keys[2] = val
            pair_5digits.remove(val)
            break
   ## get new 5
    new_keys[5] = pair_5digits[0]

    output = ''
    for val in ot:
        num = 0
        for i,key in enumerate(new_keys):
            if matched(val,new_keys[key]):
                num = key
                output += str(num)
                break
    result += int(output)

# print("part 01: ", count)

print("part 02: ",result)