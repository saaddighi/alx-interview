#!/usr/bin/python3

triangle = [[1]]

def pascal_triangle(n):
    """ a function where we can put how many rows we want."""
    if n <= 0:  
        """ returns an empty list if n <= 0"""
        return []

    for i in range(1,n): # first loop to itereat over the number of rows
        row = [1]
        for j in range(1,i): # nested loop to itereat over elements of each row
            row.append(tirangle[i-1][-j] + tirangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return tirangle
