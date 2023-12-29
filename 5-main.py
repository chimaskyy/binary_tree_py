#!/usr/bin/python3

tree_is_root = __import__("if_root").tree_is_root
from create_tree import print_binary_tree
from create_tree import binary_tree_node
from addRight import add_Right


root = binary_tree_node(98, None)
root.left = binary_tree_node(12, root)
root.right = binary_tree_node(402, root)
add_Right(54, root.left)
add_Right(128, root)
print_binary_tree(root)

rooty = tree_is_root(root)
print("Is {} a leaf: {}".format(root, rooty))
rooty = tree_is_root(root.right)
print("Is {} a leaf: {}".format(root.right, rooty))
rooty = tree_is_root(root.right.right)
print("Is {} a leaf: {}".format(root.right.right, rooty))
