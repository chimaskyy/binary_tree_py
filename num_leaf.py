#!/usr/bin/python3
from create_tree import binaryTree


class binaryTree_insert(binaryTree):
    def __init__(self, value, parent, left=None, right=None):
        super().__init__(value, parent, left, right)

    def __str__(self):
        return f"{self.value}"


def tree_leaves(root):
    """count the leaves in a binary tree"""
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    left = tree_leaves(root.left)
    right = tree_leaves(root.right)

    return left + right
