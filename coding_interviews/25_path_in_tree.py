class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def find_path(tree, num):
    ret = []
    if not tree:
        return ret

    path = [tree]
    sums = [tree.val]

    def dfs(tree):
        if tree.left:
            path.append(tree.left)
            sums.append(sums[-1] + tree.left.val)
            dfs(tree.left)
        if tree.right:
            path.append(tree.right)
            sums.append(sums[-1] + tree.right.val)
            dfs(tree.right)
        if not tree.left and not tree.right:
            if sums[-1] == num:
                ret.append([p.val for p in path])
        path.pop()
        sums.pop()

    dfs(tree)
    return ret
