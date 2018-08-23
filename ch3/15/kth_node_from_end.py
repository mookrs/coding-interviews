class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def find_kth_to_tail(head, k):
    if head is None or k <= 0:
        return None

    ahead = head
    for _ in range(k - 1):
        if ahead.next is not None:
            ahead = ahead.next
        else:
            return None

    behind = head
    while ahead.next is not None:
        ahead = ahead.next
        behind = behind.next
    return behind


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

print(find_kth_to_tail(node1, 1).val)
