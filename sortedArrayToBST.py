class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def sortedArrayToBst(nums):
    if len(nums) == 1:
        return TreeNode(nums[0])
    if len(nums) == 2:
        return TreeNode(nums[0],TreeNode(nums[1]),None)
    x = len(nums)//2
    middle = nums[x]
    arrayLeft = nums[0:x]
    arrayRight = nums[x+1:]
    res = TreeNode(middle,sortedArrayToBst(arrayLeft),sortedArrayToBst(arrayRight))
    return res



nums = [-10,-3,0,5,9]


print(sortedArrayToBst(nums))

