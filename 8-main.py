#!/usr/bin/python3

tree_depth = __import__("depth").tree_depth
from create_tree import print_binary_tree
from create_tree import binary_tree_node
from addRight import add_Right


root = binary_tree_node(98, None)
root.left = binary_tree_node(12, root)
root.right = binary_tree_node(402, root)
add_Right(54, root.left)
add_Right(128, root)

print_binary_tree(root)
depth = tree_depth(root)
print("Depth from {}: {}".format(root.value, depth))
depth = tree_depth(root.right)
print("Height from {}: {}".format(root.right.value, depth))
depth = tree_depth(root.left.right)
print("Height from {}: {}".format(root.left.right.value, depth))
