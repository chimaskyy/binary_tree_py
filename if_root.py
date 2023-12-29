#!/usr/bin/python3
from create_tree import binaryTree


class binaryTree_insert(binaryTree):
    def __init__(self, value, parent, left=None, right=None):
        super().__init__(value, parent, left, right)

    def __str__(self):
        return f"{self.value}"


def tree_is_root(node):
    if node is None:
        return False

    if node.left is not None and node.right is not None:
        return True
    else:
        return False
