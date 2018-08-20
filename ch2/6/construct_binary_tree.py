from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def bfs(self):
        ret = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return ret

    def pre_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            ret.append(head.val)
            traversal(head.left)
            traversal(head.right)

        traversal(self.root)
        return ret

    def in_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            traversal(head.left)
            ret.append(head.val)
            traversal(head.right)

        traversal(self.root)
        return ret

    def post_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            traversal(head.left)
            traversal(head.right)
            ret.append(head.val)

        traversal(self.root)
        return ret


def construct_tree(preorder=None, inorder=None):
    if not preorder or not inorder:
        # TODO 有点不理解 or
        return None
    index = inorder.index(preorder[0])
    left = inorder[0:index]
    right = inorder[index + 1:]
    root = TreeNode(preorder[0])
    root.left = construct_tree(preorder[1:1 + len(left)], left)
    root.right = construct_tree(preorder[-len(right):], right)
    return root


t = Tree()
root = construct_tree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
t.root = root
print(t.bfs())
print(t.pre_traversal())
print(t.in_traversal())
print(t.post_traversal())
