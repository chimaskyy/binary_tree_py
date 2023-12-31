#!/usr/bin/python3

one_child = __import__("one_child").one_child
from create_tree import print_binary_tree
from create_tree import binary_tree_node
from addRight import add_Right


root = binary_tree_node(98, None)
root.left = binary_tree_node(12, root)
root.right = binary_tree_node(402, root)
add_Right(54, root.left)
add_Right(128, root)

print_binary_tree(root)
node = one_child(root)
print("node in {}: {}".format(root.value, node))
node = one_child(root.right)
print("node in {}: {}".format(root.right.value, node))
node = one_child(root.left.right)
print("node in {}: {}".format(root.left.right.value, node))
