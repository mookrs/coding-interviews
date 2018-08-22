class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_node(link, node):
    if node.next is not None:
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next
        del next_node
    elif node == link:
        del node
    else:
        while link:
            if link.next == node:
                link.next = None
                del node
            link = link.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
delete_node(node1, node4)
print(node1.val, node1.next.val, node1.next.next.val)
# BUG: node3 is not original node3
delete_node(node1, node2)
print(node1.val, node1.next.val)
