class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None


def print_list_reversed1(list_node):
    stack = []

    while list_node:
        stack.append(list_node.val)
        list_node = list_node.next

    while stack:
        print(stack.pop())


def print_list_reversed2(list_node):
    if list_node:
        print_list_reversed2(list_node.next)
        print(list_node.val)


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

print_list_reversed1(node1)
print_list_reversed2(node1)
