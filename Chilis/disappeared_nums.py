'''Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once. Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.'''


def findDisappearedNumbers(nums):
    full_arr = [n for n in range(1, len(nums)+1)]
    res = list(set(full_arr) - set(nums))
    return res


print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
