#!/usr/bin/python3
from create_tree import binaryTree
from create_tree import print_binary_tree
from create_tree import binary_tree_node


class binaryTree_insert(binaryTree):
    def __init__(self, value, parent, left=None, right=None):
        super().__init__(value, parent, left, right)

    def __str__(self):
        return f"{self.value}"


def del_Tree(parent):
    if parent is None:
        return
    del_Tree(parent.left)
    del_Tree(parent.right)
    parent.left = None
    parent.right = None
