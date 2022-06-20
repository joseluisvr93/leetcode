# 168. Excel Sheet Column Title
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

def convertToTitle(n):
    """
    :type n: int
    :rtype: str
    """
    res = ''
    while n > 0:
        n -= 1
        res = chr(n % 26 + ord('A')) + res
        n //= 26
    return res

n = int(input())
print(convertToTitle(n))
