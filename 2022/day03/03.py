def day_03(file):
    X = [x.strip() for x in open(file)]
    Q = []
    p1=0
    p2=0
    group_count = 0
    group_elfs = []
    groups=  []

    for item in (X):
        half = int(len(item)/2)
        c1 = item[:half]
        c2 = item[(half):]
        l = []
        for char in c1:
            if char in c2:
                l.append(char)
        l = set(l)
        for char in l:
            if char.islower():
                p1+=ord(char)-96
            elif char.isupper():
                p1+=ord(char) - 38
    
    # part 2
    for item in X:
        if group_count < 3:
            group_count+=1
            group_elfs.append(item)  
        else:
            groups.append(group_elfs)
            group_elfs = []
            group_count = 1
            group_elfs.append(item)
    groups.append(group_elfs)

    for group in groups:
        assert len(group) == 3
        for char in group[0]:
            if (char in group[1]) and (char in group[2]):
                if char.islower():
                    p2+=ord(char)-96
                elif char.isupper():
                    p2+=ord(char) - 38
                break
    return p1, p2


for file in ['sample.txt','input.txt']:
    p1, p2 = day_03(file)
    if file == 'sample.txt':
        assert p1 == 157
        assert p2 == 70

    print(p1,p2)