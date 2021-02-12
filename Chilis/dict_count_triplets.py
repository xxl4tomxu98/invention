# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 21:39:45 2020
Took me forever to figure this out. It's a really cool problem - the breakthrough came when you realize that, since sequentiality is important, then the array should be walked in reverse because the only values you want to check are those at higher indeces than the one you are checking.
The other big thing to realize is that you're checking for two things, not just one - you're checking for the existence of a value r times the current value, or your checking for a pair that exists for the for the value that begin at r times the current value and also contain r times that value.
For example: Let's say r is 3. If you have a the value you're checking while iterating the array that is also 3, and there's a 9 and a 27 in the dictionary that you've been populating, you should have populated another dictionary and entry for the pair of the values (9, 27) because those are a pair where 27 is r times 9 and if we find a 3 at a lower index, then we know we have a triplet.
So the algorithm is: -- keep two dictionaries: 1. a dictionary to store the number of times each single value that is repeated in the array 2. a dictionary to store any pair of values that are i and (i * r) (using i as the key)
-- Walk the array backwards 1. if the pair dictionary has a value for r times the one you're checking, then you add the number of pairs to the overall count. 2. otherwise, if there's add a new pair and add it to the pair dictionary if there's a value r times the one you're checking in the single value dictionary. 3. otherwise, just add the value to the single value dictionary.
And that will do it.

In Python, O(N) time complexity:
@author: 13305
"""


def countTriplets(arr, r):
    count = 0
    dict = {}
    dictPairs = {}

    for i in reversed(arr):
        if i*r in dictPairs:
                count += dictPairs[i*r]
        if i*r in dict:
                dictPairs[i] = dictPairs.get(i, 0) + dict[i*r]

        dict[i] = dict.get(i, 0) + 1

    return count


arr = [1,3,9,27,27,81,243]
r =3
print(countTriplets(arr,r))
