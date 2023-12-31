#!/usr/bin/python3
from create_tree import binaryTree
from height import tree_height


class binaryTree_insert(binaryTree):
    def __init__(self, value, parent, left=None, right=None):
        super().__init__(value, parent, left, right)

    def __str__(self):
        return f"{self.value}"


def tree_is_full(tree):
    """check if tree is full"""
    if tree is None:
        return 0

    if tree.left is None and tree.right is None:
        return 1
    if tree.left is not None and tree.right is not None:
        return tree_is_full(tree.left) and tree_is_full(tree.right)
    return 0
