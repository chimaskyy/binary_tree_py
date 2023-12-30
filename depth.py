#!/usr/bin/python3
from create_tree import binaryTree


class binaryTree_insert(binaryTree):
    def __init__(self, value, parent, left=None, right=None):
        super().__init__(value, parent, left, right)

    def __str__(self):
        return f"{self.value}"


def tree_depth(node):
    """length of the path from the
    root node to that a node"""
    if node is None:
        return
    depth = 0
    if node.parent is not None:
        depth = 1 + tree_depth(node.parent)

    return depth
