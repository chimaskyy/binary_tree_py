#!/usr/bin/python3

tree_size = __import__("size").tree_size
from create_tree import print_binary_tree
from create_tree import binary_tree_node
from addRight import add_Right


root = binary_tree_node(98, None)
root.left = binary_tree_node(12, root)
root.right = binary_tree_node(402, root)
add_Right(54, root.left)
add_Right(128, root)

print_binary_tree(root)
size = tree_size(root)
print("Depth from {}: {}".format(root.value, size))
size = tree_size(root.right)
print("Height from {}: {}".format(root.right.value, size))
size = tree_size(root.left.right)
print("Height from {}: {}".format(root.left.right.value, size))
