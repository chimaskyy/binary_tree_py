#!/usr/bin/python3
from create_tree import binaryTree
from height import tree_height


class binaryTree_insert(binaryTree):
    def __init__(self, value, parent, left=None, right=None):
        super().__init__(value, parent, left, right)

    def __str__(self):
        return f"{self.value}"


def balance_factor(tree):
    """measure the balance factor of a tree"""
    if tree is None:
        return 0

    if tree.left is None:
        left = -1
    else:
        left = tree_height(tree.left)

    if tree.right is None:
        right = -1
    else:
        right = tree_height(tree.right)

    return left - right
