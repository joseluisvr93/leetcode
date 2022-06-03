class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root,targetSum):
    if root is None:
        return False
    if root.val == targetSum:
        return True
    return hasPathSum(root.left,targetSum-root.val) or hasPathSum(root.right,targetSum-root.val)

root = TreeNode(5,TreeNode(4,TreeNode(11,TreeNode(7),TreeNode(2)),TreeNode(8)),TreeNode(13,TreeNode(4),TreeNode(1)))
print(hasPathSum(root,22))

    

            
