def plusOne(digits):
    incrementing = 1
    res = []
    for i in range(len(digits)-1,-1,-1):
        x = digits[i] + incrementing
        if x==10:
            res.append(0)
        else:
            res.append(x)
            incrementing = 0
    if incrementing == 1:
        res.append(1)
    return res[::-1]

digits = [1,2,3]
digits = [4,3,2,1]
digits = [9]
print(plusOne(digits))
