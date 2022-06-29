# 7. Reverse Integer
# Given a 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit 
# integer range −2^31 and 2^31 − 1, then return 0.
# Example 1:
# Input: 123
# Output: 321

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x < 0:
        x = -x
        x = int(str(x)[::-1])
        x = -x
    else:
        x = int(str(x)[::-1])
    if x > 2**31 - 1 or x < -2**31:
        return 0
    return x

x = 123
print(reverse(x))
