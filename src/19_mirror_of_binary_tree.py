def mirror_recursively(root):
    if root is None or (root.left is None and root.right is None):
        return

    root.left, root.right = root.right, root.left

    if root.left is not None:
        mirror_recursively(root.left)
    if root.right is not None:
        mirror_recursively(root.right)
