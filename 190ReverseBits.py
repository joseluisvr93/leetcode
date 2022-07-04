# 170. Reverse Bits
# Reverse bits of a given 32 bits unsigned integer.
# Example 1:
# Input:    00000010100101000001111010011100
# Output:   00111001011110000010100101000000
#

def reverseBits(n):
    b = numToBin(n)
    bi = b[::-1]
    return binToNum(bi)

def numToBin(n):
    res = ""
    while n > 0:
        b = n%2
        n = n//2
        res = str(b) + res
    ad0 = "0" * (32 - len(res))
    res = ad0 + res
    return res

def binToNum(s):
    i = 0
    res = 0
    while i < len(s):
        res += (2**i) * int(s[len(s)-i-1])
        i += 1
    return res


n = 43261596
print(reverseBits(n))
n = 6
print(numToBin(n))
s = "111"
print(binToNum(s))
