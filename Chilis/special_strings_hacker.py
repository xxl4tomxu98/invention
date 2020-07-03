# Python3 program to count special
# Palindromic substring note that special palindrome only includes two different # chars, middle and side.

# Function to count special
# Palindromic susbstring


def CountSpecialPalindrome(str):
    n = len(str)

    # store count of special
    # Palindromic substring
    result = 0

    # it will store the count
    # of continues same char
    sameChar = [0] * n

    i = 0

    # traverse string character
    # from left to right
    while (i < n):

        # store same character count
        sameCharCount = 1

        j = i + 1

        # count smiler character
        while (j < n):
            if(str[i] != str[j]):
                break
            sameCharCount += 1
            j += 1

        # Case : 1
        # so total number of substring
        # that we can generate are :
        # K *( K + 1 ) / 2
        # here K is sameCharCount
        result += int(sameCharCount *
                      (sameCharCount + 1) / 2)

        # store current same char
        # count in sameChar[] array
        sameChar[i] = sameCharCount

        # increment i
        i = j

    # Case 2: Count all odd length
    # Special Palindromic substring
    for j in range(1, n):

        # if current character is equal
        # to previous one then we assign
        # Previous same character count
        # to current one
        if (str[j] == str[j - 1]):
            sameChar[j] = sameChar[j - 1]

        # case 2: odd length with middle single char case
        # only evaluate middle char and neigboring 1 other char.
        if (j > 0 and j < (n - 1) and
            (str[j - 1] == str[j + 1] and
             str[j] != str[j - 1])):
            result += (sameChar[j - 1]
                       if(sameChar[j - 1] < sameChar[j + 1])
                       else sameChar[j + 1])

    # optional is to only report the non single subtract all single
    # length substring
    return result

# This is best code I have found


def substrCount(n, s):
    count = len(s)
    for i, char in enumerate(s):
        diff_char_idx = None
        for j in range(i+1, n):
            if char == s[j]:
                if diff_char_idx is None:
                    count += 1
                elif j - diff_char_idx == diff_char_idx - i:
                    count += 1
                    break
            else:
                if diff_char_idx is None:
                    diff_char_idx = j
                else:
                    break
    return count

# traditional method


def substrCount2(n, s):

    counts = []
    # push tuples into an array for later
    for i in range(len(s)):
        if counts == []:
            counts.append([s[i], 1])
        elif s[i] == counts[-1][0]:
            counts[-1][1] = counts[-1][1] + 1
        else:
            counts.append([s[i], 1])
    # count identical chars
    ans = 0
    for pair in counts:
        ans += pair[1] * (pair[1] + 1) / 2
    # count odd palindromes with only two total chars
    for i in range(len(counts) - 2):
        if counts[i + 1][1] == 1 and counts[i][0] == counts[i + 2][0]:
            m = min(counts[i][1], counts[i + 2][1])
            ans += m

    return int(ans)

# my own brute force solution
# note this overcounts because definition of palindrome
# is different from special palindrome


def specialPalindrome(str):
    n = len(str)
    for j in range(1, n-1):
        if (same_char(str[:j]) and same_char(str[j+1:])
                and (str[j-1] == str[j+1] and str[j] != str[j-1])):
            return True
    return False


def same_char(str):
    if len(str) == 1:
        return True
    else:
        for i in range(len(str)):
            if (str[i] != str[0]):
                return False
        return True


def substrCount3(n, str):
    result = []
    count = 0
    for length in range(1, n+1):
        for i in range(n-length+1):
            sub = str[i:i+length]
            if same_char(sub) or specialPalindrome(sub):
                result.append(sub)
                count += 1

    return count


# Driver Code
str = "abcbaba"
print(CountSpecialPalindrome(str))
print(substrCount(7, str))
print(substrCount2(7, str))
print(substrCount3(7, str))
# This code is contributed by mits.
