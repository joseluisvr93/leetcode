class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def isSameTree(p,q):
    if q is None and p is None:
        return True
    elif q is None or p is None:
        return False
    elif p.val != q.val:
        return False
    elif not isSameTree(p.left,q.left):
        return False
    elif not isSameTree(p.right,q.right):
        return False
    return True


p = TreeNode(1,TreeNode(2),TreeNode(3))
q = TreeNode(1,TreeNode(2),TreeNode(3))
p = TreeNode(1,TreeNode(2),None)
q = TreeNode(1,None,TreeNode(2))
p = TreeNode(1,TreeNode(1),None)
q = TreeNode(1,None,TreeNode(1))

print(isSameTree(q,p))
