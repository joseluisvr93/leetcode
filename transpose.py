def transpose(matrix):
    x = len(matrix)
    y = len(matrix[0])
    res = []
    for i in range(y):
        temp = []
        for j in range(x):
            temp.append(matrix[j][i])
        res.append(temp)
    return(res)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))
