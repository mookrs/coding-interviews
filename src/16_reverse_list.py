class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head):
    reversed_head = None
    node = head
    prev = None
    while node is not None:
        next = node.next

        if next is None:
            reversed_head = node

        node.next = prev
        prev = node
        node = next
    return reversed_head


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3
p = reverse_list(node1)
print(p.val)
