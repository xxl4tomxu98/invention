# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 19:38:11 2020

@author: 13305
"""

def droppedRequest(RequestTime):
    D = {}
    for i in RequestTime:
        if i in D:
            D[i] += 1
        else:
            D[i] = 1
        drop_count = 0
        time = [i for i in D]
        time.sort()
        for i in time:
            drop_count += max(D[i]-3,0)
            drop_count += max(sum([D[i] for i in range(max(min(time),i-9),i+1) if i in D])-20,0)
            drop_count += max(sum([D[i] for i in range(max(min(time),i-59),i+1) if i in D])-60,0)
    return drop_count

RequestTime = [1,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,11,11,11,6,6,6,5,5,5]
drop_count = droppedRequest(RequestTime)
print(drop_count)
