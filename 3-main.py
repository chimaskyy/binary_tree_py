#!/usr/bin/python3

del_Tree = __import__("delTree").del_Tree
from create_tree import print_binary_tree
from create_tree import binary_tree_node
from addRight import add_Right

root = binary_tree_node(98, None)

root.left = binary_tree_node(12, root)
root.right = binary_tree_node(402, root)
add_Right(54, root.left)
add_Right(128, root.left)
print_binary_tree(root)
del_Tree(root)
