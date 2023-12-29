#!/usr/bin/python3

add_Right = __import__("addRight").add_Right
from create_tree import print_binary_tree
from create_tree import binary_tree_node


root = binary_tree_node(98, None)

root.left = binary_tree_node(12, root)
root.right = binary_tree_node(402, root)
print_binary_tree(root)

print()

add_Right(128, root.left)
add_Right(54, root)

print_binary_tree(root)
