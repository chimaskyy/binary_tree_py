#!/usr/bin/python3

binary_tree_node = __import__("create_tree").binary_tree_node

root = binary_tree_node(5, None)

root.left = binary_tree_node(34, root)
root.left.left = binary_tree_node(3, root.left)
root.left.right = binary_tree_node(56, root.left)
root.right = binary_tree_node(9, root)
root.right.left = binary_tree_node(20, root.right)
root.right.right = binary_tree_node(8, root.right)

from create_tree import print_binary_tree

print_binary_tree(root)
