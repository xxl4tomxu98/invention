"""Sam is part of the organizing team arranging the university's career fair and has list of companies and their respective arrival times and durations. Due to university-wide budget cuts, there is only one stage/dais available on the entire campus so only one event can occur at a time. Given each company's arrival time and the duration they will stay, determine the maximum number of promotional events that can be hosted during the career fair. For example, there are n = 5 companies that will arrive at times arrival = [1, 3, 3, 5, 7] and will stay for duration = [2, 2, 1, 2, 1). The first company arrives at time 1 and stays for 2 hours. At time 3, two companies arrive, but only 1 can stay for either 1 or 2 hours. The next companies arrive at times 5 and 7 and do not conflict with each other. In total, there can be a maximum of 4 promotional events. Function Description Complete the function maxEvents in the editor below. It must return an integer that represents the maximum number of promotional events that can be hosted. maxEvents has the following parameter(s): arrival/arrival[O]....arrival[n-1]]: an array of integers where ith element is the arrival time of the ith company. duration[duration (O)....duration[n 1]]: an array of integers where th element is the duration that the ith company's stay at the career fair. Constraints • 1<n< 50 • 1 s arrival[i] 1000 • 1< duration[i] < 1000 • Both 'arrival' array and duration' array will have equal number of elements"""

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxEvents' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arrival
#  2. INTEGER_ARRAY duration
#

def maxEvents(arrival, duration):
    # Write your code here
    events = [0]
    arr_sorted, dur_sorted = zip(*sorted(zip(arrival, duration)))
    for i in range(len(arrival)-1):
        if arr_sorted[events[-1]]+dur_sorted[events[-1]] <= arr_sorted[i+1]:
            events.append(i+1)
        elif arr_sorted[events[-1]]+dur_sorted[events[-1]] >= arr_sorted[i+1]+dur_sorted[i+1]:
            events.pop()
            events.append(i+1)
    return len(events)

if __name__ == '__main__':
