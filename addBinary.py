def addBinary(a,b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    x = binaryToInt(a)
    y = binaryToInt(b)
    z = x + y
    return intToBinary(z)
    
    # return bin(int(a,2) + int(b,2))[2:]

def binaryToInt(a):
    """
    :type a: str
    :rtype: int
    """
    res = 0
    for i in range(len(a)):
        res += int(a[len(a)-1-i])*pow(2,i)
    return res

def intToBinary(a):
    """
    :type a: int
    :rtype: str
    """
    res = ""
    if a == 0:
        return "0"
    else:
        while a > 0:
            res = str(a%2) + res
            a = a//2
        return res


a = "11"
b = "1"
a = "0"
b = "0"
print(addBinary(a,b))
