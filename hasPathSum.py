class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root,targetSum):
    right = False
    left = False
    if root is None:
        return False
    if root.val == targetSum and root.left is None and root.right is None:
        return True
    if root.left is not None:
        root.left.val += root.val 
        left = hasPathSum(root.left,targetSum)
    if root.right is not None:
        root.right.val += root.val 
        right = hasPathSum(root.right,targetSum)
    return right or left

root = TreeNode(5,TreeNode(4,TreeNode(11,TreeNode(7),TreeNode(2)),TreeNode(8)),TreeNode(13,TreeNode(4),TreeNode(1)))
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(hasPathSum(root,22))

    

            
