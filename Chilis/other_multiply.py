# Find a new array that each index is filled with product of
# all other elements in the array except the indexed one

import math


def other_multiply(arr):
    arr1 = []
    for ind in range(len(arr)):
        b = [x for i, x in enumerate(arr) if i != ind]
        arr1.append(math.prod(b))
    return arr1


print(other_multiply([1, 2, 3]))
