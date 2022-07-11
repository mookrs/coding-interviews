class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge(head1, head2):
    if head1 is None:
        return head2
    elif head2 is None:
        return head1

    merged_head = None
    if head1.val < head2.val:
        merged_head = head1
        merged_head.next = merge(head1.next, head2)
    else:
        merged_head = head2
        merged_head.next = merge(head1, head2.next)

    return merged_head


node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node1.next = node2
node2.next = node3

node4 = ListNode(2)
node5 = ListNode(4)
node6 = ListNode(6)
node4.next = node5
node5.next = node6

p = merge(node1, node4)
print(p.val, p.next.val, p.next.next.val)
