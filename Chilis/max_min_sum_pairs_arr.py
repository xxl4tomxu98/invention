"""Minimum and Maximum sum of absolute differences of pairs

Given an array of N integers where N is even, find the minimum and maximum sum
of the absolute difference of N/2 pairs formed by pairing every element with
one other element.

Ex: Input: a[] = {10, -10, 20, -40}
Output: min_sum = 40, max_sum = 80
Explanation: Pairs selected for minimum sum
             (-10, -40) and (10, 20)
             min_sum = |-10 - -40| + |20 - 10| = 40
             Pairs selected for maximum sum
             (-10, 20) and (-40, 10)
             max_sum = |-10 - 20| + |10 - -40| = 80

Input: a[] = {20, -10, -1, 30}
Output: min_sum = 19, max_sum = 61
Explanation: Pairs selected for minimum sum
             (-1, -10) and (20, 30)
             min_sum = |-1 - -10| + |20 - 30| = 19
             Pairs selected for maximum sum
             (-1, 30) and (-10, 20)
             max_sum = |-1 - 30| + |-10 - 20| = 61 """


# function to calculate minimum sum
def calculate_min_sum(a, n):

    # sorts the array a
    a.sort()

    # initially min=0 and max=0
    min_sum = 0

    # traverse to find the minimum sum
    for i in range(1, n, 2):

        # the adjacent elements difference
        # will always be smaller
        min_sum += abs(a[i] - a[i - 1])

    return min_sum


# function to calculate maximum sum
def calculate_max_sum(a, n):

    # sorts the array a
    a.sort()

    max_sum = 0

    # traverse to find the maximum sum
    for i in range(n // 2):

        # the farthest distant elements sum
        max_sum += abs(a[n - 1 - i] - a[i])
    return max_sum


print(calculate_max_sum([20, -10, -1, 30], 4))
print(calculate_min_sum([20, -10, -1, 30], 4))
