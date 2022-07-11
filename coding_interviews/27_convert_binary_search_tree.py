class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def convert(root):
    if not root:
        return None
    last = convert_node(root, None)

    head = last
    while head and head.left:
        head = head.left
    return head


def convert_node(node, last):
    if not node:
        return None

    if node.left:
        last = convert_node(node.left, last)

    node.left = last
    # 上一个节点不为空，即当前结点不是第一个结点
    if last:
        last.right = node
    last = node

    if node.right:
        last = convert_node(node.right, last)

    return last
