# 171. Excel Sheet Column Number
# Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
# Example 1:
# Input: "A"
# Output: 1
# Example 2:
# Input: "AB"
# Output: 28

def titleToNumber(columnTitle):
    res = 0
    m = 0
    for letter in columnTitle:
        number = (ord(letter) - 64)
        res += number * (26**(len(columnTitle)-m-1))
        m += 1
    return res

columnTitle = "AAAA"
# columnTitle = "AA"
# columnTitle = "FXSHRXW"
columnTitle = "AB"
print(titleToNumber(columnTitle))
