# Given non empty binary tree, calculate average of the node
# values on each level of the tree in the form of a array


class TreeNode:
    def __init__(self, val):
        self._value = val
        self._left = None
        self._right = None


def binary_tree_level_avg(root):
    queue = [root]
    result = []

    while queue:
        sum = 0
        count = len(queue)
        # traverse breadth first and sum up values
        for i in range(count):
            popped = queue.pop(0)
            sum += float(popped._value)
            if popped._left:
                queue.append(popped._left)
            if popped._right:
                queue.append(popped._right)
        result.append(sum/count)
    return result


node_a = TreeNode('3')
node_b = TreeNode('9')
node_c = TreeNode('20')
node_d = TreeNode('15')
node_e = TreeNode('7')

node_a._left = node_b
node_a._right = node_c
node_c._left = node_d
node_c._right = node_e


print(binary_tree_level_avg(node_a))
