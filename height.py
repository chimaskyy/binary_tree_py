#!/usr/bin/python3
from create_tree import binaryTree


class binaryTree_insert(binaryTree):
    def __init__(self, value, parent, left=None, right=None):
        super().__init__(value, parent, left, right)

    def __str__(self):
        return f"{self.value}"


def tree_height(parent):
    if parent is None:
        return

    if parent.left is not None:
        left_h = 1 + tree_height(parent.left)
    else:
        left_h = 0

    if parent.right is not None:
        right_h = 1 + tree_height(parent.right)
    else:
        right_h = 0

    if left_h > right_h:
        return left_h
    else:
        return right_h
