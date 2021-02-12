'''In this section we are going to find the first unique or non-repeating
character from a string or stream of characters. There are multiple ways
to solve this problem. We will try to create two different program for the
same stream of characters.

Method 1: HashMap and Two-string method traversals.

Approach: A character is said to be non-repeating if its frequency in the
string is unit. Now for finding such characters, one needs to find the
frequency of all characters in the string and check which character has
unit frequency. This task could be done efficiently using a hash_map which
will map the character to their respective frequencies and in which we can
simultaneously update the frequency of any character we come across in
constant time. The maximum distinct characters in the ASCII system are 256.
So hash_map has a maximum size of 256. Now read the string again and the
first character which we find has a frequency as unity is the answer.

Algorithm:

Make a hash_map which will map the character to there respective frequencies.
Traverse the given string using a pointer.
Increase the count of current character in the hash_map.
Now traverse the string again and check whether the current character
hasfrequency=1. If the frequency>1 continue the traversal.
Else break the loop and print the current character as the answer.
Pseudo Code :

for ( i=0 to str.length())
  hash_map[str[i]]++;

for(i=0 to str.length())
  if(hash_map[str[i]]==1)
  return str[i]
  break

Method 2: HashMap and single string traversal.

Approach: Make a count array instead of hash_map of maximum number of
characters(256). We can augment the count array by storing not just
counts but also the index of the first time you encountered the
character e.g. (3, 26) for ‘a’ meaning that ‘a’ got counted 3 times
and the first time it was seen is at position 26. So when it comes to
finding the first non-repeater, we just have to scan the count array,
instead of the string. Thanks to Ben for suggesting this approach.

Algorithm :

Make a count_array which will have two fields namely frequency, first
occurence of a character. The size of count_array is ‘256’.
Traverse the given string using a pointer.
Increase the count of current character and update the occurence.
Now here’s a catch, the array will contain valid first occurence of the
character which has frequency has unity otherwise the first occurence keeps
updating. Now traverse the count_array and find the character which has least
value of first occurence and frequency value as unity. Return the character
Pseudo Code :

for ( i=0 to str.length())
count_arr[str[i]].first++;
count_arr[str[i]].second=i;

int res=INT_MAX;
for(i=0 to count_arr.size())
  if(count_arr[str[i]].first==1)
  res=min(min, count_arr[str[i]].second)

return res


'''

# Method2


def firstNonRepeatingChar(str1):
    char_order = []
    counts = {}
    for c in str1:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
            char_order.append(c)
    for c in char_order:
        if counts[c] == 1:
            return c
    return None


print(firstNonRepeatingChar('PythonforallPythonMustforall'))
print(firstNonRepeatingChar('tutorialspointfordeveloper'))
print(firstNonRepeatingChar('AABBCC'))


# Method 1.
# Python program to print the first non-repeating character
NO_OF_CHARS = 256


# Returns an array of size 256 containg count
# of characters in the passed char array
def getCharCountArray(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)] += 1
    return count


# The function returns index of first non-repeating
# character in a string. If all characters are repeating
# then returns -1
def firstNonRepeating(string):
    count = getCharCountArray(string)
    index = -1
    k = 0

    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1

    return index


# Driver program to test above function
string = "geeksforgeeks"
index = firstNonRepeating(string)
if index == 1:
    print("Either all characters are repeating or string is empty")
else:
    print("First non-repeating character is " + string[index])
