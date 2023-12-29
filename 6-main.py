#!/usr/bin/python3

preOrder = __import__("preorder").preOrder
from create_tree import print_binary_tree
from create_tree import binary_tree_node
from preorder import inOrder, postOrder


root = binary_tree_node(98, None)
root.left = binary_tree_node(12, root)
root.right = binary_tree_node(402, root)
root.left.left = binary_tree_node(6, root.left)
root.left.right = binary_tree_node(56, root.left)
root.right.left = binary_tree_node(256, root.right)
root.right.right = binary_tree_node(512, root.right)

print_binary_tree(root)
preOrder(root)
print()
inOrder(root)
print()
postOrder(root)
