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

#a simplified version of countingSort()
def countingSort(the_list, max_value):
    # Count the number of times each value appears.
    # counts[0] stores the number of 0's in the input
    # counts[4] stores the number of 4's in the input
    # etc.
    counts = [0] * (max_value + 1)
    for item in the_list:
        counts[item] += 1
    # Overwrite counts to hold the next index an item with
    # a given value goes. So, counts[4] will now store the index
    # where the next 4 goes, not the number of 4's our
    # list has. This is essentially cumulative approach above
    num_items_before = 0
    for i, count in enumerate(counts):
        counts[i] = num_items_before
        num_items_before += count
    # Output list to be filled in
    sorted_list = [None] * len(the_list)
    # Run through the input list
    for item in the_list:
        # Place the item in the sorted list
        sorted_list[ counts[item] ] = item
        # And, make sure the next item we see with the same value
        # goes after the one we just placed
        counts[item] += 1
    return sorted_list


expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
d = 5

print(activityNotifications(expenditure, d))
