# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 10:51:28 2020

@author: 13305
"""


# !/bin/python3


import os


# Complete the minimumSwaps function below.

def minimumSwaps(arr):
    arr = [x-1 for x in arr]
    count = 0
    i = 0
    while i < len(arr):
        if arr[i] != i:
            temp = arr[i]
            arr[temp], arr[i] = arr[i], arr[temp]
            count += 1
        else:
            i += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
