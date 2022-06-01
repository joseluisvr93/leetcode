class ListNode:
    def __init__(self, val=0, next=None):
        """
        :type val: int
        :type next: ListNode
        """
        self.val = val
        self.next = next

def mergeTwoLists(list1 ,list2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    result = ListNode()
    tail = result
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    return result.next

list1 = ListNode(1,ListNode(2,ListNode(4)))
list2 = ListNode(1,ListNode(3,ListNode(4)))

res = mergeTwoLists(list1,list2)

while res.next is not None:
    print(res.val,end=" ")
    res = res.next
print(res.val)
