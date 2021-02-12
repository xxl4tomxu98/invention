
'''Dynamic Programming with Binary Search
Algorithm

In this approach, we scan the array from left to right. We also make use of a
dpdp array initialized with all 0's. This dpdp array is meant to store the
increasing subsequence formed by including the currently encountered element.
While traversing the numsnums array, we keep on filling the dpdp array with
the elements encountered so far. For the element corresponding to the j^{th}j
th
  index (nums[j]nums[j]), we determine its correct position in the dpdp
  array(say i^{th}i
th
  index) by making use of Binary Search(which can be used since the dpdp array
  is storing increasing subsequence) and also insert it at the correct
  position. An important point to be noted is that for Binary Search,
  we consider only that portion of the dpdp array in which we have made
  the updates by inserting some elements at their correct positions
  (which remains always sorted). Thus, only the elements upto the i^{th}i
th
  index in the dpdp array can determine the position of the current element in
  it. Since, the element enters its correct position(ii) in an ascending order
  in the dpdp array, the subsequence formed so far in it is surely an
  increasing subsequence. Whenever this position index ii becomes
  equal to the length of the LIS formed so far(lenlen), it means,
  we need to update the lenlen as len = len + 1len=len+1.

Note: dpdp array does not result in longest increasing subsequence,
but length of dpdp array will give you length of LIS.

Consider the example:

input: [0, 8, 4, 12, 2]

dp: [0]

dp: [0, 8]

dp: [0, 4]

dp: [0, 4, 12]

dp: [0 , 2, 12] which is not the longest increasing subsequence, but length
of dpdp array results in length of Longest Increasing Subsequence. '''


# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minDeletions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def search_index(A, l, r, key):
    while (r - l > 1):
        m = l + (r - l)//2
        if (A[m] >= key):
            r = m
        else:
            l = m
    return r


def minDeletions(arr):
    n = len(arr)
    dp = [0]*n
    length = 0
    for my_int in arr:
        i = search_index(dp, 0, length, my_int)
        if i < 0:
            i = -(i + 1)
        dp[i] = my_int
        if i == length:
            length += 1
    if length >= n-1:
        deletion = 0
    else:
        deletion = n - length
    return deletion


if __name__ == '__main__':
