#!/usr/bin/python3
"""a typical interview question or test that is asked
    """


def minOperations(n) -> int:
    """a function that takes a number(n) and returns the number of operations
    needed to have H n number of times in a file using only the copy all and
    paste operations"""
    if n <= 1:
        return 0

    op = 0
    for i in range(2, n + 1):
        while n % i == 0:
            n //= i
            op += i
    if n == 1:
        return op
    else:
        return 0
