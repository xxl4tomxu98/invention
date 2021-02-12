"""Given an array of integers, sort the array in ascending order using the
Bubble Sort algorithm above. Once sorted, print the following three lines:

Array is sorted in numSwaps swaps., where  is the number of swaps that took
place. First Element: firstElement, where  is the first element in the sorted
array. Last Element: lastElement, where  is the last element in the sorted
array. Hint: To complete this challenge, you must add a variable that keeps
a running tally of all swaps that occur during execution.

For example, given a worst-case but small array to sort:  we go through the
following steps:

swap    a
0       [6,4,1]
1       [4,6,1]
2       [4,1,6]
3       [1,4,6]
It took  swaps to sort the array. Output would be

Array is sorted in 3 swaps.
First Element: 1
Last Element: 6
Function Description

Complete the function countSwaps in the editor below. It should print the
three lines required, then return.

countSwaps has the following parameter(s):

a: an array of integers .
Input Format

The first line contains an integer, , the size of the array .
The second line contains  space-separated integers .

Constraints

Output Format

You must print the following three lines of output:

Array is sorted in numSwaps swaps., where  is the number of swaps that took
place.First Element: firstElement, where  is the first element in the sorted
array.Last Element: lastElement, where  is the last element in the sorted array."""


def countSwaps(a):
    count = 0
    for j in range(len(a)):
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                count += 1
    print('Array is sorted in ' + str(count) + ' swaps.')
    print('First Element: ' + str(a[0]))
    print('Last Element: ' + str(a[-1]))


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
