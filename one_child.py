#!/usr/bin/python3
from create_tree import binaryTree


class binaryTree_insert(binaryTree):
    def __init__(self, value, parent, left=None, right=None):
        super().__init__(value, parent, left, right)

    def __str__(self):
        return f"{self.value}"


def one_child(node):
    """count node with atleast 1 child"""
    if node is None:
        return 0

    if node.left is None and node.right is None:
        return 0

    left = one_child(node.left)
    right = one_child(node.right)

    return left + right + 1
