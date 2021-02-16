# give int array sorted return each element sqaured and sorted
# has to be O(n), e.g. can not use .sort or sorted() which is
# at least O(nlog(n)) This is iterative tabulation method
# where traverse of the original arr is like the merge method
# in merge_sort() that is O(n) n is the total array length

def sorted_squared_arr(array):
    n = len(array)
    result = [0] * n
    i = 0
    j = n-1
    for k in range(n):
        if abs(array[i]) > abs(array[j]):
            result[n-1-k] = array[i]*array[i]
            i += 1
        else:
            result[n-1-k] = array[j]*array[j]
            j -= 1

    return result


print(sorted_squared_arr([-9, -6, -2, 2, 3, 6, 8, 9]))
