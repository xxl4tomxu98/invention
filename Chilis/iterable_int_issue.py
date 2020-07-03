# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 16:56:35 2020

@author: 13305
"""

# This is demo on 'int' array slicer not iterable
# can't do slicing, has to do looping
# Complete the arrayManipulation function below.


def arrayManipulation(n, queries):

    arr = [0]*n
    l = list(queries)
    for i in range(len(l)):
        a = queries[i][0]
        b = queries[i][1]
        k = queries[i][2]
        for j in range(a-1, b):
            arr[j] += k
        print(arr)
    return max(arr)


queries = [[2, 3, 5],
           [1, 5, 10],
           [2, 6, 20]]

print(arrayManipulation(10, queries))
