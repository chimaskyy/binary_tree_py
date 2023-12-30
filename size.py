#!/usr/bin/python3
from create_tree import binaryTree


class binaryTree_insert(binaryTree):
    def __init__(self, value, parent, left=None, right=None):
        super().__init__(value, parent, left, right)

    def __str__(self):
        return f"{self.value}"


def tree_size(root):
    if root is None:
        return 0

    if root is not None:
        left = tree_size(root.left)
        right = tree_size(root.right)

        return 1 + left + right
