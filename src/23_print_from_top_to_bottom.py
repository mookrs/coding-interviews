from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bfs(tree):
    if not tree:
        return []

    q = deque()
    q.append(tree)
    ret = []
    while q:
        node = q.popleft()
        ret.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return ret
