#!/bin/python3

import math
import os
import random
import re
import sys



import functools

def log(descriptor):
    def func_decorator(func):
       
        # @functools.wraps(func)
        def wrapper(*args):
            descriptor.write(f'LOG: {func.__name__}{str(args).replace(" ", "")}\n')
            return func(*args)
        
        return wrapper
    return func_decorator

if __name__ == '__main__':
    file_path = f'{os.path.abspath(os.path.dirname(__file__))}/file.txt'
    fptr = open(file_path, 'w')

    @log(fptr)
    def my_max(a, b, c):
        return max(a, b, c)


    @log(fptr)
    def my_min(a, b):
        return min(a, b)


    @log(fptr)
    def my_sum(*args):
        return sum(args)


    q = int(input())
    for _ in range(q):
        line = input().split()
        f_name, params = line[0], map(int, line[1:])
        if f_name == "my_min":
            res = my_min(*params)
            fptr.write(f"{res}\n")
        elif f_name == "my_max":
            res = my_max(*params)
            fptr.write(f"{res}\n")
        elif f_name == "my_sum":
            res = my_sum(*params)
            fptr.write(f"{res}\n")
        else:
            raise ValueError("Unknown function name %s" % f_name)
    fptr.close()
    

'''
possible input:

1
my_max 1 2 3
'''


'''
Remotebase domain test questions:
1. reverge args
- user args keyword and simple .reverse() to reverse the arguments

2. map with lambda
- use of list comprehension
- lambda x : pow(int(i),2) for i in x if int(i)>0
    above statement is ~ to
    for i in x:
        if int(i)>0:
            pow(int(i),2)
- need to map a list of list with specific comditions

3. decoratos
- most complicated one
- a decorator takes an argument so have to create another internal function whose default argument is functiion name
- in order to read argumnet parameters, had to create another internal method
- imported functools (but dont really need it)
- this was also done but couldnt submit only because was unable to remove space from the tuple
    - used str(args).replace(" ", "") for it after wards

Topics:
- list comprehensions
- decorators
- args
- lambda and map
'''