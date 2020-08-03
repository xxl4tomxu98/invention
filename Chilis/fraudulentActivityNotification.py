# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 15:21:26 2020

@author: 13305
"""


#import numpy as np

def activityNotifications(expenditure, d):
  n = len(expenditure)
  #expenditure = np.array(expenditure)
  count = 0
  for i in range(d, n):
    countingSort(expenditure[i-d:i])
    print(expenditure)
    if d%2 == 0 and (expenditure[i] >= (expenditure[i-(d//2)-1]+expenditure[i-(d//2)])):
      count += 1
    elif d%2 !=0 and (expenditure[i] >= 2*expenditure[i-(d//2)-1]):
      count += 1
  return count

def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]

expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
d = 5

print(activityNotifications(expenditure, d))
