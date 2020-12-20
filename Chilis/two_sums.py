'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
 '''


def two_sums(nums, target):
    res = []
    i = 0
    while(i != len(nums)):
        if nums.count(target-nums[i]) != 0 and nums.index(target-nums[i]) != i:
            res.append(i)
            res.append(nums.index(target-nums[i]))
            i = len(nums)
        else:
            i += 1
    return res


print(two_sums([2, 7, 11, 15], 9))
