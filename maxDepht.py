class TreeNode:
     """docstring for TreeNode"""
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def maxDepth(root):
    depth = 0
    if root is None:
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    if left > right:
        depth += left
    else:
        depth += right
    return depth + 1

root = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
print(maxDepth(root))
