# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 10:47:21 2020

@author: 13305
"""


# Complete the minimumBribes function below.

def minimumBribes(q):
    count = 0
    # adjust the queue integers(1,2,3..) to indexes(0,1,2,3..)
    q = [x-1 for x in q]
    # we want to check how many times a particular person in queue having been bribed
    for i in range(len(q)):
        # forward moving maximum is 2 bribes, q[i] is previous index, i is current index
        if q[i] - i > 2:
            # any person can't be bribed more than twice
            print('Too chaotic')
            return
        # count how many time i has been bribed, if previous index is lower than current one
        for j in range(max(q[i]-1, 0), i):
            if q[j] > q[i]:
                count += 1
    print(count)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
