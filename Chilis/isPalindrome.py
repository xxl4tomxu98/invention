'''Write a function that takes a string and returns
true if it's a palindrome, false if it's not.
This solution takes less time and memory than rebuilding
the string backward and comparing the two.
time O(n)
space O(1)
'''


def isPalindrome(str):
    for idx, char in enumerate(str):
        if str[idx] != str[len(str)-1-idx]:
            return False
    return True


def is_palindrome(str):
    return str[::1] == str[::-1]


print(isPalindrome("linterretnil"))
print(is_palindrome("linterretnil"))
