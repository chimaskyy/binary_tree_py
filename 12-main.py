#!/usr/bin/python3

balance_factor = __import__("balance").balance_factor
from create_tree import print_binary_tree
from create_tree import binary_tree_node
from addRight import add_Right
from addLeft import add_Left


root = binary_tree_node(98, None)
root.left = binary_tree_node(12, root)
root.right = binary_tree_node(402, root)
add_Right(54, root.left)
add_Right(128, root)
add_Left(45, root)
add_Right(50, root.left)
add_Left(10, root.left.left)
add_Left(8, root.left.left.left)


print_binary_tree(root)
node = balance_factor(root)
print("balance of {}: {}".format(root.value, node))
node = balance_factor(root.right)
print("balance of {}: {}".format(root.right.value, node))
node = balance_factor(root.left.left.right)
print("balance of {}: {}".format(root.left.left.right.value, node))
