"""Maximize the last Array element as per the given conditions
Last Updated: 24-08-2020
Given an array arr[] consisting of N integers, rearrange the array such that it satisfies the following conditions:

arr[0] must be 1.
Difference between adjacent array elements should not exceed 1, that is, arr[i] – arr[i-1] ≤ 1 for all 1 ≤ i < N.
The permissible operations are as follows:

Rearrange the elements in any way.
Reduce any element to any number ≥ 1.
The task is to find the maximum possible value that can be placed at the last index of the array.

Examples:

Input: arr[] = {3, 1, 3, 4}
Output: 4
Explanation:
Subtracting 1 from the first element modifies the array to {2, 1, 3, 4}.
Swapping the first two elements modifes the array to {1, 2, 3, 4}.
Therefore, maximum value placed at the last index is 4.



Input: arr[] = {1, 1, 1, 1}
Output: 1

Recommended: Please try your approach on {IDE} first, before moving on to the solution.
Approach:
To solve the given problem, sort the given array and balance it according to the given condition starting from left towards right. Follow the below steps to solve the problem:

Sort the array in ascending order.
If the first element is not 1, make it 1.
Traverse the array over the indices [1, N – 1) and check if every adjacent element has a difference of ≤ 1.
If not, decrement the value till the difference becomes ≤ 1.
Return the last element of the array. """


#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMaxValue' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getMaxValue(arr):
    # Write your code here
    n = len(arr)
    arr.sort();
    if (arr[0] != 1):
        arr[0] = 1;
    for i in range(1, n):
        if (arr[i] - arr[i - 1] > 1):
            arr[i] = arr[i - 1] + 1;
    return arr[n - 1];

if __name__ == '__main__':
