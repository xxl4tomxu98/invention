'''Segregate Even and Odd numbers
Difficulty Level : Easy
 Last Updated : 30 Sep, 2020
Given an array A[], write a function that segregates even and odd numbers.
The functions should put all even numbers first, and then odd numbers.
Example:
Input  = {12, 34, 45, 9, 8, 90, 3}
Output = {12, 34, 8, 90, 45, 9, 3}

In the output, the order of numbers can be changed, i.e., in the above example,
34 can come before 12 and 3 can come before 9.

The problem is very similar to our old post Segregate 0s and 1s in an array,
and both of these problems are variation of famous Dutch national flag problem.

Algorithm: segregateEvenOdd()
1) Initialize two index variables left and right:
            left = 0,  right = size -1
2) Keep incrementing left index until we see an odd number.
3) Keep decrementing right index until we see an even number.
4) If lef < right then swap arr[left] and arr[right]
'''


# Python program to segregate even and odd elements of array

def segregateEvenOdd(arr):

    # Initialize left and right indexes
    left, right = 0, len(arr)-1

    while left < right:

        # Increment left index while we see 0 at left
        while (arr[left] % 2 == 0 and left < right):
            left += 1

        # Decrement right index while we see 1 at right
        while (arr[right] % 2 == 1 and left < right):
            right -= 1

        if (left < right):
            # Swap arr[left] and arr[right]*/
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right = right-1


# Driver function to test above function
arr = [12, 34, 45, 9, 8, 90, 3]
segregateEvenOdd(arr)

print("Array after segregation "),
for i in range(0, len(arr)):
    print(arr[i])
# This code is contributed by Devesh Agrawal
