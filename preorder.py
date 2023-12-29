#!/usr/bin/python3
from create_tree import binaryTree


class binaryTree_insert(binaryTree):
    def __init__(self, value, parent, left=None, right=None):
        super().__init__(value, parent, left, right)

    def __str__(self):
        return f"{self.value}"


def preOrder(root):
    if root is None:
        return False
    print(root.value, end=" ")
    preOrder(root.left)
    preOrder(root.right)


def inOrder(root):
    if root is None:
        return False
    inOrder(root.left)
    print(root.value, end=" ")
    inOrder(root.right)


def postOrder(root):
    if root is None:
        return False
    postOrder(root.left)
    postOrder(root.right)
    print(root.value, end=" ")
