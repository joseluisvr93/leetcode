class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2 : ListNode):
    while list1.next is not None:
        print(list1.val)
        list1 = list1.next
    return 0

list1 = ListNode(1,ListNode(2,ListNode(4)))
list2 = ListNode(1,ListNode(3,ListNode(4)))

mergeTwoLists(list1,list2)

