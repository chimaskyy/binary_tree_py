#!/usr/bin/python3

add_Left = __import__("addLeft").add_Left
from create_tree import print_binary_tree
from create_tree import binary_tree_node


root = binary_tree_node(98, None)

root.left = binary_tree_node(12, root)
root.right = binary_tree_node(402, root)
print_binary_tree(root)

print()

add_Left(128, root.right)
add_Left(54, root)

print_binary_tree(root)
