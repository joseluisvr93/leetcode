# 4th bit
# a binary number is a combination of 1s and 0s. Its n least significant digit is the n digit starting from the right starting with 1.
# Given a decimal number, convert it to binary and find the 4th least significant bit.

def fourth_bit(n):
    return (n >> 3) & 1

n = 77
print(fourth_bit(n))

def fourth_bit_2(n):
    return n >> 4

n = 77
print(fourth_bit(n))
