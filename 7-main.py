#!/usr/bin/python3

tree_height = __import__("height").tree_height
from create_tree import print_binary_tree
from create_tree import binary_tree_node
from addRight import add_Right


root = binary_tree_node(98, None)
root.left = binary_tree_node(12, root)
root.right = binary_tree_node(402, root)
add_Right(54, root.left)
add_Right(128, root)

print_binary_tree(root)
height = tree_height(root)
print("Height from {}: {}".format(root.value, height))
height = tree_height(root.right)
print("Height from {}: {}".format(root.right.value, height))
height = tree_height(root.left.right)
print("Height from {}: {}".format(root.left.right.value, height))
