class TreeNode:
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left 
        self.right = right

def isSymmetric(root):
    if root.left is None and root.right is None:
        return True
    elif root.left is None:
        return False
    elif root.right is None:
        return False
    elif isSameTree(root.left, root.right):
        return True
    return False

def isSameTree(p,q):
    if q is None and p is None:
        return True
    elif q is None or p is None:
        return False
    elif p.val != q.val:
        return False
    elif not isSameTree(p.left,q.right):
        return False
    elif not isSameTree(p.right,q.left):
        return False
    return True

root = TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(2,TreeNode(4),TreeNode(3)))

print(isSymmetric(root))
