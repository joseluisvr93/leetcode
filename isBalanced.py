class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    if root is None:
        return True
    left = depht(root.left)
    right = depht(root.right)
    if left > 2:
        if isBalanced(root.left) != True:
            return False
    if right > 2:
        if isBalanced(root.right) != True:
            return False
    if abs(left-right) < 2:
        return True
    else:
        return False

def depht(root):
    left = 0
    right = 0
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is not None:
        left += depht(root.left) 
    if root.right is not None:
        right += depht(root.right) 
    if right > left: 
        return right + 1
    else:
        return left + 1

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.left.left = TreeNode(4)
# root.right = TreeNode(2)
# root.right.right = TreeNode(3)
# root.right.right.right = TreeNode(4)

root = TreeNode(1) 
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)

print(isBalanced(root))
