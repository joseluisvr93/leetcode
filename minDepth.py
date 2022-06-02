class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root):
    if root is None:
        return 0
    left = 9999
    right = 9999
    if root.left is None and root.right is None:
        return 1
    if root.right is not None:
        right = minDepth(root.right)
    if root.left is not None:
        left = minDepth(root.left)
    if left < right:
        return left + 1
    else:
        return right + 1

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(minDepth(root))
