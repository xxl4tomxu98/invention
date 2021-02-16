'''Find the lowest common ancestor of two nodes in a binary
search tree.Assume I give you both the root and the two nodes.
In this solution, we can simply use the BST property to find
the lowest common ancestor in O(log(n)) time. We know that for
two nodes, if one of the nodes is on the left of the parent and
one is on the right (or if one of the nodes is the parent),
the parent must be the lowest common ancestor. Otherwise,
if both nodes are on the left or right, there must be a lower
common ancestor so we search that side. This solution takes
O(log(n)) where n is the number of nodes because in the worst case,
we will have to traverse the height of the tree.'''


class TreeNode:
    def __init__(self, value):
        self._left = None
        self._right = None
        self._value = value


class BinarySearchTree:
    def __init__(self, value):
        self._root = None
        self._value = value
        self._left = None
        self._right = None

    # TODO: Implement node value insertion method
    def insert_value(self, value, current_node=False):
        if not current_node:
            node = TreeNode(value)
            if not self._root:
                self._root = node
                return self._root
            else:
                current_node = self._root
                if (value < current_node._value) and current_node._left:
                    current_node = current_node._left
                if (value >= current_node._value) and current_node._right:
                    current_node = current_node._right
                if (not current_node._left) and (value < current_node._value):
                    current_node._left = node
                if (not current_node._right) and (value >=
                                                  current_node._value):
                    current_node._right = node


def lowest_common_ancester(root, node1, node2):
    current_node = root
    while True:
        if current_node == node1 or current_node == node2:
            return current_node._value
        both_on_left = (node1._value < current_node._value and
                        node2._value < current_node._value)
        both_on_right = (node1._value >= current_node._value and
                         node2._value >= current_node._value)
        if not(both_on_left or both_on_right):
            return current_node._value
        else:
            current_node = current_node._left if both_on_left else \
                        current_node._right


tree = BinarySearchTree(3)
tree.insert_value(10)
tree.insert_value(5)
tree.insert_value(16)
tree.insert_value(1)
tree.insert_value(7)
tree.insert_value(16)
print(tree._root._value)                  # 10
print(tree._root._left._value)            # 5
print(tree._root._right._value)           # 16
print(tree._root._left._left._value)      # 1
print(tree._root._left._right._value)     # 7
print(tree._root._right._right._value)    # 16
print(lowest_common_ancester(tree._root, tree._root._left,
                             tree._root._left._left))
