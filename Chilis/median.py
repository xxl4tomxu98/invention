'''Given two sorted arrays, find the median element amongst the two arrays.
That is, if both arrays were combined, find the median element from the
combined array. Assume that there is not enough memory to actually combine
both arrays. There exists an O(log n + log m) solution.
Solution
Since they are sorted, you can find the middle element of each to find the
medians of each list. The actual median is now somewhere in between these
two numbers. You can then discard the non-relevant portions of each list.
Repeat the process. When the middle elements from both lists converge,
you have now found the median element.

To make two halves, make the partition such that the index that partitioning
array A[] + the index that partitioning array B[] are equal to the total
number of elements plus one divided by 2, i.e. (n + m + 1) / 2 (+1 is, if
the total number of elements is odd).

First, define two variables : min_index and max_index, and initialize
min_index to 0, and max_index to the length of the smaller array.
In these below examples A[] is the smaller array.
To partition A[], use the formula (min_index + max_index) / 2 and insert
it to a variable i. To partition B[], use the formula (n + m + 1) / 2 – i
and insert it to a variable j. the variable i means the number of elements
to be inserted from A[] into the first half, and j means the number of
elements to be inserted from B[] into the first half, the rest of the
elements will be inserted into the second half.
'''


# Python code for median with
# case of returning double
# value when even number
# of elements are present
# in both array combineed
median = 0
i = 0
j = 0


# def to find max
def maximum(a, b):
    return a if a > b else b


# def to find minimum
def minimum(a, b):
    return a if a < b else b


# def to find median
# of two sorted arrays
def findMedianSortedArrays(a, n, b, m):

    global median, i, j
    min_index = 0
    max_index = n

    while (min_index <= max_index):
        i = (min_index + max_index) // 2
        j = ((n + m + 1) // 2) - i

        # if i = n, it means that
        # Elements from a[] in the
        # second half is an empty
        # set. and if j = 0, it
        # means that Elements from
        # b[] in the first half is
        # an empty set. so it is
        # necessary to check that,
        # because we compare elements
        # from these two groups.
        # Searching on right
        if (i < n and j > 0 and b[j - 1] > a[i]):
            min_index = i + 1

        # if i = 0, it means that
        # Elements from a[] in the
        # first half is an empty
        # set and if j = m, it means
        # that Elements from b[] in
        # the second half is an empty
        # set. so it is necessary to
        # check that, because we compare
        # elements from these two groups.
        # searching on left
        elif (i > 0 and j < m and b[j] < a[i - 1]):
            max_index = i - 1

        # we have found the
        # desired halves.
        else:
            # this condition happens when
            # we don't have any elements
            # in the first half from a[]
            # so we returning the last
            # element in b[] from the
            # first half.
            if (i == 0):
                median = b[j - 1]

            # and this condition happens
            # when we don't have any
            # elements in the first half
            # from b[] so we returning the
            # last element in a[] from the
            # first half.
            elif (j == 0):
                median = a[i - 1]
            else:
                median = maximum(a[i - 1], b[j - 1])
            break

    # calculating the median.
    # If number of elements
    # is odd there is
    # one middle element.

    if ((n + m) % 2 == 1):
        return median

    # Elements from a[] in the
    # second half is an empty set.
    if (i == n):
        return ((median + b[j]) / 2.0)

    # Elements from b[] in the
    # second half is an empty set.
    if (j == m):
        return ((median + a[i]) / 2.0)

    return ((median + minimum(a[i], b[j])) / 2.0)


# This is a easier to understand by merge sort
def find_merged_median(arr1, arr2):
    i1 = 0
    i2 = 0
    len1 = len(arr1)
    len2 = len(arr2)
    totalLen = len1 + len2
    if totalLen == 0:
        return None
    totalArr = []
    while i1 < len1 and i2 < len2:
        if arr1[i1] <= arr2[i2]:
            totalArr.append(arr1[i1])
            i1 += 1
        else:
            totalArr.append(arr2[i2])
            i2 += 1

    while i1 < len1:
        totalArr.append(arr1[i1])
        i1 += 1

    while i2 < len2:
        totalArr.append(arr2[i2])
        i2 += 1

    if totalLen % 2 != 0:
        return totalArr[(totalLen - 1) / 2]
    else:
        return (totalArr[totalLen // 2] + totalArr[totalLen // 2 - 1])/2


# Driver code
a = [900]
b = [10, 13, 14]
n = len(a)
m = len(b)

# we need to define the
# smaller array as the
# first parameter to make
# sure that the time complexity
# will be O(log(min(n,m)))
if (n < m):
    print("The median is : {}".format(findMedianSortedArrays(a, n, b, m)))
else:
    echo("The median is : {}".format(findMedianSortedArrays(b, m, a, n)))


print(find_merged_median(a, b))
