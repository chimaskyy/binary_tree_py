#!/usr/bin/python3

tree_leaves = __import__("num_leaf").tree_leaves
from create_tree import print_binary_tree
from create_tree import binary_tree_node
from addRight import add_Right


root = binary_tree_node(98, None)
root.left = binary_tree_node(12, root)
root.right = binary_tree_node(402, root)
add_Right(54, root.left)
add_Right(128, root)

print_binary_tree(root)
n_leaf = tree_leaves(root)
print("Leaves in {}: {}".format(root.value, n_leaf))
n_leaf = tree_leaves(root.right)
print("Leaves in {}: {}".format(root.right.value, n_leaf))
n_leaf = tree_leaves(root.left.right)
print("Leaves in {}: {}".format(root.left.right.value, n_leaf))
