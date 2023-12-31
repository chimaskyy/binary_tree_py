#!/usr/bin/python3

tree_is_full = __import__("full").tree_is_full
from create_tree import print_binary_tree
from create_tree import binary_tree_node
from addRight import add_Right
from addLeft import add_Left


root = binary_tree_node(98, None)
root.left = binary_tree_node(12, root)
root.right = binary_tree_node(402, root)
add_Right(54, root.left)
add_Right(128, root)
root.left.left = binary_tree_node(10, root.left)


print_binary_tree(root)
node = tree_is_full(root)
print("Is {} full: {}".format(root.value, node))
node = tree_is_full(root.left)
print("Is {} full: {}".format(root.left.value, node))
node = tree_is_full(root.right)
print("Is {} full: {}".format(root.right.value, node))
