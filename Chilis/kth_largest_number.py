import sys

'''Given an array and a number k where k is smaller than size of array,
we need to find the k’th smallest element in the given array.
It is given that all array elements are distinct.

Examples:

Input: arr[] = {7, 10, 4, 3, 20, 15}
k = 3
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}
k = 4
Output: 10 '''


'''A simple solution is to sort the given array using a O(N log N)
sorting algorithm like Merge Sort, Heap Sort, etc and return the
element at index k-1 in the sorted array.
Time Complexity of this solution is O(N Log N) '''


# Python3 program to find k'th smallest element
# Function to return k'th smallest
# element in a given array
def kthSmallest(arr, n, k):

    # Sort the given array
    arr.sort()

    # Return k'th element in the
    # sorted array
    return arr[k-1]


# Driver code
if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    n = len(arr)
    k = 2
    print("K'th smallest element is",
          kthSmallest(arr, n, k))


''' This is an optimization "quickselect" if QuickSort is used as a
sorting algorithm in first step. In QuickSort, we pick a pivot element,
then move the pivot element to its correct position and partition the
array around it. The idea is, not to do complete quicksort, but stop at
the point where pivot itself is k’th smallest element. Also, not to
recur for both left and right sides of pivot, but recur for one of them
according to the position of pivot. The worst case time complexity of
this method is O(n2), but it works in O(n) on average. '''


# This function returns k'th smallest element
# in arr[l..r] using QuickSort based method.
# ASSUMPTION: ALL ELEMENTS IN ARR[] ARE DISTINCT


def kthSmallest(arr, low, high, k):

    # If k is smaller than number of
    # elements in array
    if (k > 0 and k <= high - low + 1):

        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        pos = partition(arr, low, high)

        # If position is same as k
        if (pos - low == k - 1):
            return arr[pos]
        if (pos - low > k - 1):  # If position is more,
            # recur for left subarray
            return kthSmallest(arr, low, pos - 1, k)

        # Else recur for right subarray
        return kthSmallest(arr, pos + 1, high,
                           k - pos + low - 1)

    # If k is more than number of
    # elements in array
    return sys.maxsize

# Standard partition process of QuickSort().
# It considers the last element as pivot and
# moves all smaller element to left of it
# and greater elements to right


def partition(arr, low, high):
    x = arr[high]
    i = low
    for j in range(low, high):
        if (arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


# Driver Code
if __name__ == "__main__":

    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 3
    print("Kth smallest element is",
          kthSmallest(arr, 0, n - 1, k))
