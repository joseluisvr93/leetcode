# Given an integer numRows, generate the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.

def generate(numRows):
    res=[]
    res.append([1])
    if numRows == 1:
        return res
    res.append([1,1])
    if numRows == 2:
        return res

    for i in range(2,numRows):
        temp = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(res[i-1][j-1]+res[i-1][j])
        res.append(temp)
    return res

n = 8
print(generate(n))


