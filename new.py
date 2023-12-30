#!/usr/bin/python3


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        if value > self.value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def add_Left(self, value, root):
        if root is None:
            return

        new_node = Node(value)

        if root.left is not None:
            new_node.left = root.left
            root.left = new_node

        root.left = new_node

        return new_node

    def add_Right(self, value, root):
        if root is None:
            return

        new_node = Node(value)

        if root.right is not None:
            new_node.right = root.right
            root.right = new_node

        root.right = new_node

        return new_node

    def del_tree(self, root):
        if root is None:
            return
        self.del_tree(root.left)
        self.del_tree(root.right)
        root.left = None
        root.right = None

    def node_is_leaf(self, root):
        if root is None:
            return False

        if root.left is None and root.right is None:
            return True
        else:
            return False

    def is_root(self, node):
        if node is None:
            return False

        if node.left is not None and node.right is not None:
            return True
        else:
            return False

    def tree_height(self, root):
        if root is None:
            return
        if root.left is not None:
            left_h = 1 + self.tree_height(root.left)
        else:
            left_h = 0
        if root.right is not None:
            right_h = 1 + self.tree_height(root.right)
        else:
            right_h = 0

        if left_h > right_h:
            return left_h
        else:
            return right_h


def preOrder(root):
    if root is None:
        return

    print(root.value, end=" ")
    preOrder(root.left)
    preOrder(root.right)


def postOrder(root):
    if root is None:
        return

    postOrder(root.left)
    postOrder(root.right)
    print(root.value, end=" ")


def inOrder(root):
    if root is None:
        return

    inOrder(root.left)
    print(root.value, end=" ")
    inOrder(root.right)


root = Node(5)
root.insert(3)
root.insert(7)
root.insert(2)
root.insert(4)
root.add_Left(34, root)
"""root.add_Left(23, root.right)
root.add_Left(9, root.right)
root.add_Right(20, root)
root.add_Right(78, root.right)
root.add_Right(43, root.right)
# root.del_tree(root)
# root = None"""


preOrder(root)
print()
postOrder(root)
print()
inOrder(root)
print()

ret = root.is_root(root.left)
print("is node {} root: {}".format(root.left.value, ret))

height = root.tree_height(root)
print(height)
