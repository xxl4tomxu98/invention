class TreeNode:
    def __init__(self, val):
        self._value = val
        self._left = None
        self._right = None


def invert_binary_tree(node):
    if not node:
        return
    node._left, node._right = node._right, node._left
    invert_binary_tree(node._left)
    invert_binary_tree(node._right)


def in_order_traversal(root):
    if not root:
        return []
    left = in_order_traversal(root._left)
    right = in_order_traversal(root._right)
    return [*left] + [root._value] + [*right]


node_a = TreeNode('3')
node_b = TreeNode('9')
node_c = TreeNode('20')
node_d = TreeNode('15')
node_e = TreeNode('7')

node_a._left = node_b
node_a._right = node_c
node_c._left = node_d
node_c._right = node_e

print(in_order_traversal(node_a))

invert_binary_tree(node_a)

print(in_order_traversal(node_a))
