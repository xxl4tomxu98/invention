'''Smallest substring with each letter occurring both in uppercase and
lowercase.

Given a string S of length N, the task is to find the smallest balanced
substring in S. If no such substring is present, print -1. A string is
balanced if every letter in the string appears in both uppercase and
lowercase, i.e “AabB” is a
balanced string whereas “Ab” is not a balanced string.

Examples:

Input: S = “azABaabba”
Output: ABaab
Explanation:
Substring {S[2], …, S[6]} (0-based indexing) smallest substring which is
balanced.

Input: S = “Technocat”
Output: -1

Naive Approach: The simplest approach is to generate all possible substrings
of the given string and check if there exists any substring satisfying the
given conditions. Print the smallest of all such substrings.

Time Complexity: O(N3)
Auxiliary Space: O(N)

Efficient Approach: To optimize the above approach, the idea is to use the
concept of Sliding Window. Follow the steps below to solve the problem:

Traverse the given string and store the characters whose only lowercase or
uppercase form are present in the input string in a Map mp. Initialize
two arrays to keep track of the lowercase and uppercase characters obtained
so far.
Now, traverse the string maintaining two pointers i and st
(initialized with 0), where st will point to the start of the current
substring and i will point to the current character. If the current
character is in mp, neglect all the
characters obtained so far and start from the next character and adjust the
arrays accordingly. If the current character is not in mp, remove the extra
characters from the beginning of the substring with the help of st pointer,
such that the frequency of any character does not convert to 0
and adjust the arrays accordingly.

Now, check whether the substring {S[st], ….., S[i]} is balanced or not. If
balanced and i – st + 1 is smaller than the length of balanced substring
obtained so far.
Update the length and also store the start and end indices of the substring,
i.e. st and i respectively. Repeat the steps till the end of the string.'''

# python 3 program for the above approach
import sys
# Function to check if the current
# string is balanced or not


def balanced(small, caps):
    # For every character, check if
    # there exists uppercase as well
    # as lowercase characters
    for i in range(26):
        if (small[i] != 0 and (caps[i] == 0)):
            return 0
        elif((small[i] == 0) and (caps[i] != 0)):
            return 0
    return 1
# Function to find smallest length substring
# in the given string which is balanced


def smallestBalancedSubstring(s):
    # Store frequency of
    # lowercase characters
    small = [0 for i in range(26)]
    # Stores frequency of
    # uppercase characters
    caps = [0 for i in range(26)]
    # Count frequency of characters
    for i in range(len(s)):
        if (ord(s[i]) >= 65 and ord(s[i]) <= 90):
            caps[ord(s[i]) - 65] += 1
        else:
            small[ord(s[i]) - 97] += 1
    # Mark those characters which
    # are not present in both
    # lowercase and uppercase
    mp = {}
    for i in range(26):
        if (small[i] and caps[i] == 0):
            mp[chr(i + 97)] = 1
        elif (caps[i] and small[i] == 0):
            mp[chr(i + 65)] = 1
    # Initialize the frequencies
    # back to 0
    for i in range(len(small)):
        small[i] = 0
        caps[i] = 0
    # Marks the start and
    # end of current substring
    i = 0
    st = 0
    # Marks the start and end
    # of required substring
    start = -1
    end = -1
    # Stores the length of
    # smallest balanced substring
    minm = sys.maxsize
    while (i < len(s)):
        if(s[i] in mp):
            # Remove all characters
            # obtained so far
            while (st < i):
                if (ord(s[st]) >= 65 and ord(s[st]) <= 90):
                    caps[ord(s[st]) - 65] -= 1
                else:
                    small[ord(s[st]) - 97] -= 1
                st += 1
            i += 1
            st = i
        else:
            if (ord(s[i]) >= 65 and ord(s[i]) <= 90):
                caps[ord(s[i]) - 65] += 1
            else:
                small[ord(s[i]) - 97] += 1
            # Remove extra characters from
            # front of the current substring
            while (1):
                if (ord(s[st]) >= 65 and ord(s[st]) <= 90
                    and caps[ord(s[st]) - 65] > 1):
                    caps[ord(s[st]) - 65] -= 1
                    st += 1
                elif (ord(s[st]) >= 97 and ord(s[st]) <= 122
                      and small[ord(s[st]) - 97] > 1):
                    small[ord(s[st]) - 97] -= 1
                    st += 1
                else:
                    break
            # If substring (st, i) is balanced
            if (balanced(small, caps)):
                if (minm > (i - st + 1)):
                    minm = i - st + 1
                    start = st
                    end = i
            i += 1
    # No balanced substring
    if (start == -1 or end == -1):
        print(-1)
    # Store answer string
    else:
        ans = ""
        for i in range(start, end + 1, 1):
            ans += s[i]
        print(ans)

# Driver Code
if __name__ == '__main__':

    # Given string
    s = "azABaabba"
    smallestBalancedSubstring(s)
