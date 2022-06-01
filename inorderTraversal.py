class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def inorderTraversal(root):
    res = []
    if root is not None:
        if root.left is not None:
            res.extend(inorderTraversal(root.left))
        res.append(root.val)
        if root.right is not None:
            res.extend(inorderTraversal(root.right))
    return res


root = TreeNode(1,None,TreeNode(2,TreeNode(3),None))
print(inorderTraversal(root))
