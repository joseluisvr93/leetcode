class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2 : ListNode):
    if list1 is None and list2 is None:
        return None
    elif list1 is None:
        return list2
    elif list2 is None:
        return list1
    listResult = ListNode()
    while list1.next is not None and list2.next is not None:
        if list1.val > list2.val:
            print(list1.val)
            list1 = list1.next
        else:
            print(list2.val)
            list2 = list2.next
    return listResult

list1 = ListNode(1,ListNode(2,ListNode(4)))
list2 = ListNode(1,ListNode(3,ListNode(4)))

res = mergeTwoLists(list1,list2)

while res.next is not None:
    print(res.val)
    res = res.next
print(res.val)
