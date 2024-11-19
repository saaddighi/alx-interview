def pascal_triangle(n):
    if n <= 0:
       return []
    triangle = [[1]]
    for i in range(1,n):
        row = [1]
        for j in range(1,i):
            row.append(triangle[i-1][-j] + triangle[i-1][j])
            print(row)
        row.append(1)
        print(row)
        triangle.append(row)
    return triangle

print(pascal_triangle(2))
       