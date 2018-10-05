class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def has_subtree(root1, root2):
    result = False

    if root1 is not None and root2 is not None:
        if root1.val == root2.val:
            result = does_tree1_have_tree2(root1, root2)
        if not result:
            result = has_subtree(root1.left, root2)
        if not result:
            result = has_subtree(root1.right, root2)

    return result


def does_tree1_have_tree2(root1, root2):
    if root2 is None:
        return True
    if root1 is None:
        return False
    if root1.val != root2.val:
        return False

    return does_tree1_have_tree2(root1.left, root2.left) and does_tree1_have_tree2(root1.right, root2.right)


root1 = TreeNode(8)
root2 = TreeNode(8)
root3 = TreeNode(7)
root4 = TreeNode(9)
root5 = TreeNode(2)
root6 = TreeNode(4)
root7 = TreeNode(7)
root1.left = root2
root1.right = root3
root2.left = root4
root2.right = root5
root5.left = root6
root5.right = root7

root8 = TreeNode(8)
root9 = TreeNode(9)
root10 = TreeNode(2)
root8.left = root9
root8.right = root10

print(has_subtree(root1, root8))
