class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    flag = 0
    res = None
    while headA is not None and headB is not None:
        if headA.val == headB.val:
            if res is None:
                res = ListNode(headA.val)
            headA = headA.next
            headB = headB.next
            flag = 1
        else:
            flag = 0
            res = None
    return res




