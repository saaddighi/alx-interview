#!/usr/bin/python3
"""a typical interview question or test that is asked
    """

def minOperations(n) -> int:
    """a function that takes a number(n) and returns the number of operations
    needed to have H n number of times in a file using only the copy all and 
    paste operations"""
    op = 0
    if n % 2 == 0:
        with open('test.txt', 'r') as file:
    
            char = file.read()
            ch = char*2
        op = 1 + (n // 2)
        for i in range((n // 2)):
            with open ('tst.txt','a') as d_file:
                d_file.write(ch)
        with open('tst.txt', 'r') as d_file:
            res = d_file.read()
        return op 
    elif n % 3 == 0:
        with open('test.txt', 'r') as file:
            
            char = file.read()
            ch = char*3
            op = 3 + (n // 3)
        for i in range((n // 3)):
            with open ('tst.txt','a') as d_file:
                d_file.write(ch)
        with open('tst.txt', 'r') as d_file:
            res = d_file.read()
        return op

    else:
        return 0
