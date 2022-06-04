# Given an integer numRows, generate the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.

def generate(numRows):
    if numRows == 1:
        return [1]
    if numRows == 2:
        return [1,1]
    res = [1] * numRows
    last1 = 1
    last2 = 1
    for i in range(numRows//2):
        res[i+1] =  last+2
        res[numRows-i-2] =  i+2

    return res

n = 5
print(generate(n))


