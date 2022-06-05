# 119 Pascal's Triangle ii
# https://leetcode.com/problems/pascals-triangle-ii
# Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1, 1]
    row = [1, 1]
    for i in range(2, rowIndex + 1):
        row = [1] + [row[j] + row[j + 1] for j in range(len(row) - 1)] + [1]
    return row

rowIndex = 8
print(getRow(rowIndex))
