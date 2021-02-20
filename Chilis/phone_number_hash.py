'''Vanity phone numbers are often displayed with letters instead of numbers,
such as 1800flowers (18003569377). Write a program that, when provided with
a potential phone number (3569377) and word (flower), returns all combinations
containing the search word ("flowerp", "flowerq", "flowerr", "flowers").
For reference the numbers of a phone kepad map to letters as shown in the hash
below. Note 0 and 1 do not have corresponding letters. Digit to Letter hash:
0: [""]
1: [""]
2: ["a","b","c"]
3: ["d","e","f"]
4: ["g","h","i"]
5: ["j","k","l"]
6: ["m","n","o"]
7: ["p","q","r","s"]
8: ["t","u","v"]
9: ["w","x","y","z"]

Example:
1. Given "228" and "cat", matching strings would be "cat".
2. Given "2283" and "cat", matching strings would be "catd", "cate", "catf".
3. Given "52283" and "cat", matching strings would be "jcatd", "jcate",
"jcatf", "kcatd", "kcate", "kcatf", "lcatd", "lcate", "lcatf".

Bonus:
Vanity phone numbers often include numbers, as in 1-866-4ZIPCAR (1-866-4947227)
where the number 4 is a homonym for 'for'. Expand the above algorithm to
include the ability to match numbers in the search string.
Example:
Given "242287" and "4cats", matching strings would be "a4cats", "b4cats",
"c4cats", "24cats".'''


dictionary = {'0': [""],
              '1': [""],
              '2': ["a", "b", "c"],
              '3': ["d", "e", "f"],
              '4': ["g", "h", "i"],
              '5': ["j", "k", "l"],
              '6': ["m", "n", "o"],
              '7': ["p", "q", "r", "s"],
              '8': ["t", "u", "v"],
              '9': ["w", "x", "y", "z"]}


def digits_to_words(digits, subString):
    result = ['']
    intermediate = []
    # find the index of the first occurance of subString digit
    if subString[0] != '4':
        index = next(digits.find(i) for i, val in dictionary.items()
                     if subString[0] in val)
    else:
        index = digits.find('4')
    # digits starts with non subString containing digit
    if index > 0:
        for digit in digits[:index]:
            char_list = dictionary[digit]
            if subString[0] == '4':
                char_list.append(digit)
            # eliminate "0" and "1"
            if 0 == len(char_list):
                continue
            for word_str in result:
                for suffix in char_list:
                    intermediate.append(word_str + suffix)
            # assign intermediate to result and reset it
            result = intermediate
            intermediate = []
        result = [res + subString for res in result]
    # digits starts with subString containing digit
    elif index == 0:
        result = [subString]
    # finish rest of digits that does not contain subString
    for digit in digits[len(result[0]):]:
        char_list = dictionary[digit]
        # eliminate "0" and "1"
        if 0 == len(char_list):
            continue
        for word_str in result:
            for suffix in char_list:
                intermediate.append(word_str + suffix)
        # assign intermediate to result and reset it
        result = intermediate
        intermediate = []
    return result


print(digits_to_words("228", "cat"))
print(digits_to_words("2283", "cat"))
print(digits_to_words("52283", "cat"))
print(digits_to_words('242287', '4cats'))
print(digits_to_words('64947227', '4zipcar'))
print(digits_to_words("542283", "4cat"))
