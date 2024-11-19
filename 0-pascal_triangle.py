#!/usr/bin/python3

tirangle = [[1]]

def pascal_triangle(n):
    if n <= 0:
        return []

    for i in range(1,n):
        row = [1]
        for j in range(1,i):
            row.append(tirangle[i-1][-j] + tirangle[i-1][j])
        row.append(1)
        tirangle.append(row)
    return tirangle
