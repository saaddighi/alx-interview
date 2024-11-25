def minOperations(n):
    lst = []
    if n % 2:  # Check if n is odd
        # Read the content of 'test.txt'
        with open('test.txt', 'r') as file:
            char = file.read()
        
        # Write the content to 'tst.txt'
        with open('tst.txt', 'w') as d_file:
            d_file.write(char)
        
        # Append char*2 for n//2 times (use integer division)
        for i in range(n // 2):  # Using integer division for proper range
            with open('tst.txt', 'a') as d_file:
                d_file.write(char * 2)  # Append the content twice
        
        # Read the final content from 'tst.txt'
        with open('tst.txt', 'r') as d_file:
            res = d_file.read()
    
    else:
        res = ""  # Initialize res to an empty string if n is even or 0
    
    return res

# Call the function
result = minOperations(8)
print(result)
