"""The absolute difference is the positive difference between two values a
and b, is written |a-b| or  |b-a|and they are equal. Function Description:

Complete the minimumAbsoluteDifference function in the editor below. It should
return an integer that represents the minimum absolute difference between any
pair of elements.

minimumAbsoluteDifference has the following parameter(s):

int arr[n]: an array of integers
Returns

int: the minimum absolute difference found
Input Format

The first line contains a single integer , the size of .
The second line contains  space-separated integers, .

Constraints

Sample Input 0

3
3 -7 0
Sample Output 0

3
Explanation 0

The first line of input is the number of array elements. The array,[3,-7,0].
There are three pairs to test: (3, -7), (3,0) , and (-7, 0).
The absolute differences are 10, 3, 7 respectively:

Remember that the order of values in the subtraction does not influence
the result. The smallest of these absolute differences is 3.

Sample Input 1

10
-59 -36 -13 1 -53 -92 -2 -96 -54 75
Sample Output 1

1
Explanation 1

The smallest absolute difference is abs(-53 -(-54)) = 1.

Sample Input 2

5
1 -3 71 68 17
Sample Output 2

3
Explanation 2

The minimum absolute difference is 71-68 = 3."""


# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    diff = 2*10**9
    for i in range(1, len(arr)):
        diff = min(diff, arr[i] - arr[i-1])
    return diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
