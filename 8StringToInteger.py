# 8. String to Integer (atoi)
# Implement the myatoi(string s) function which converts a string to an integer 32-bit signed integer.
# The algorithm for myAtoi(string s) is:
# 1. Read in and ignore any leading whitespace.
# 2. Check if the first character is a - or +. Read this character in if it is either.
#    This determines if the final result is negative or positive respectively.
#    Asume positive if no sign is found.
# 3. Read in the next character until a non-digit character or the end of the input is reached.
#    The rest of the string is ignored
# 4. Convert these digits into an integer. if no digit were found, then the integer is 0.
#    Change the sign as necessary.
# 5. If the integer is out of the range of [-2**31, 2**31-1], then clamp the integer so that it remains  in the range.
#    Specifically if the integer is less then -2**31 should be clamped to -2**31 and if the integer is greater than 2**31-1 then clamp to 2**31-1.
# 6. Return the integer as the final result.

def myAtoi(s):
    for letter in s:
        print()
