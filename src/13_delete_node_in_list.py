class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_node(list_head, to_be_deleted):
    if to_be_deleted.next is not None:
        next_node = to_be_deleted.next
        to_be_deleted.val = next_node.val
        to_be_deleted.next = next_node.next
        del next_node
    elif list_head == to_be_deleted:
        del to_be_deleted
    else:
        node = list_head
        while node.next != to_be_deleted:
            node = node.next
        node.next = None
        del to_be_deleted


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4

delete_node(node1, node3)
print(node1.next.next.val)
delete_node(node1, node3)
print(node1.next.val)
delete_node(node1, node1)
print(node1.val)
delete_node(node1, node1)
print(node1.val)
