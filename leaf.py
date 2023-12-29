#!/usr/bin/python3
from create_tree import binaryTree


class binaryTree_insert(binaryTree):
    def __init__(self, value, parent, left=None, right=None):
        super().__init__(value, parent, left, right)

    def __str__(self):
        return f"{self.value}"


def tree_is_leaf(parent):
    if parent is None:
        return False

    if parent.left is None and parent.right is None:
        return True
    else:
        return False
