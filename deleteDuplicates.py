class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    if head is None:
        return head

    result = ListNode()
    tail = result

    tail.val = head.val
    head = head.next
    while head is not None:
        if head.val == tail.val:
            head = head.next
        else:
            tail.next = ListNode(head.val)
            tail = tail.next
    return result

head = ListNode(1,ListNode(1,ListNode(2)))
head = ListNode(1,ListNode(1,ListNode(2,ListNode(3,ListNode(3)))))

res = deleteDuplicates(head)

while res.next is not None:
    print(res.val,end=" ")
    res = res.next
print(res.val)
