from collections import defaultdict, Counter
import copy
import math
import datetime

class Monkey:
    def __init__(self):
        self.count = 0
        self.name = None
        self.items = []
        self.op = None
        self.div = 0
        self.friend1 = None
        self.friend2 = None

    def throw(self, item):
        if(item % self.div) == 0:
            return self.friend1
        else:
            return self.friend2
    
    def update_item_level(self, item):
        '''
        sets new worry level of item after monkeys inspection
        '''
        self.count += 1
        op, factor = self.op.split()
        if factor == 'old':
            factor = item
        if op == '*':
            return item * int(factor)
        elif op == '+':
            return item + int(factor)


def day_11(file, composite_no):
    p1 = 0
    p2 = 0

    monkeys = []
    rounds = 10000

    with open(file) as f:
        for line in f:
            monkey = Monkey()
            monkey.name = int(line.strip().split(" ")[1].strip(':'))
            monkey.items = [int(x) for x in f.readline().split(':')[1].split(',')]
            monkey.op = f.readline().split('old ')[1].strip()
            monkey.div = int(f.readline().split('by')[1].strip())
            monkey.friend1 = int(f.readline().split('monkey')[1].strip())
            monkey.friend2 = int(f.readline().split('monkey')[1].strip())
            f.readline()
            monkeys.append(monkey)
        
        # print("total monkey: ", len(monkeys))
        
        # starting rounds
        start = datetime.datetime.now()
        for r in range(rounds):
            for monkey in monkeys:
                for item in monkey.items:
                    new_item = monkey.update_item_level(item) % composite_no
                    new_mon = monkey.throw(new_item)
                    monkeys[new_mon].items.append(new_item)
                monkey.items = []
            # print("round ended in ",start - datetime.datetime.now())
        business = [monkey.count for monkey in monkeys]
        business.sort()
        p1 = business[-1]*business[-2]

    return p1, p2


for file, composite_no in [('sample.txt', 96577), ('input.txt', 9699690)]:
    p1, p2 = day_11(file, composite_no)

    # check if the test example passess
    # if file == 'sample.txt':
    #     assert p1 == 11
    #     assert p2 == 26

    print(p1,p2)
