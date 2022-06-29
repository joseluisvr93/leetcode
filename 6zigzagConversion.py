# 6. Zigzag Conversion
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows 
# like this: (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);
# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
        return s
    row = [''] * numRows
    index = 0
    down = False
    for c in s:
        row[index] += c
        if index == 0 or index == numRows - 1:
            down = not down
        index += 1 if down else -1
    return ''.join(row)

s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))
