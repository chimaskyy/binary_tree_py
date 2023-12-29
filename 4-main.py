#!/usr/bin/python3

tree_is_leaf = __import__("leaf").tree_is_leaf
from create_tree import print_binary_tree
from create_tree import binary_tree_node
from addRight import add_Right


root = binary_tree_node(98, None)
root.left = binary_tree_node(12, root)
root.right = binary_tree_node(402, root)
add_Right(54, root.left)
add_Right(128, root)
print_binary_tree(root)

leafy = tree_is_leaf(root)
print("Is {} a leaf: {}".format(root, leafy))
leafy = tree_is_leaf(root.right)
print("Is {} a leaf: {}".format(root.right, leafy))
leafy = tree_is_leaf(root.right.right)
print("Is {} a leaf: {}".format(root.right.right, leafy))
