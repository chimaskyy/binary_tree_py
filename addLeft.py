#!/usr/bin/python3


class binaryTree:
    def __init__(self, value, parent, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.value}"


def add_Left(value, parent):
    if parent is None:
        return

    new_node = binaryTree(value, parent)

    if parent.left is not None:
        new_node.left = parent.left
        parent.left.parent = new_node

    parent.left = new_node

    return new_node


def print_binary_tree(node, level=0, right=None):
    if node is not None:
        if node.right is not None:
            print_binary_tree(node.right, level + 1, right=True)

        print("\t" * level + f".-------({node})-------.")

        if node.left is not None:
            print_binary_tree(node.left, level + 1, right=False)
