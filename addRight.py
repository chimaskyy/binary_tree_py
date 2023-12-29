#!/usr/bin/python3
from create_tree import binaryTree


class binaryTree_insert(binaryTree):
    def __init__(self, value, parent, left=None, right=None):
        super().__init__(value, parent, left, right)

    def __str__(self):
        return f"{self.value}"


def add_Right(value, parent):
    if parent is None:
        return

    new_node = binaryTree(value, parent)

    if parent.right is not None:
        new_node.right = parent.right
        parent.right.parent = new_node

    parent.right = new_node

    return new_node
