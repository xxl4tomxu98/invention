'''Take an input string and return a string that is made up of the number of occurences of each english letter in the input followed by that letter, sorted alphabetically. The output string shouldn't contain chars missing from input (chars with 0 occurence); leave them out.
An empty string, or one with no letters, should return an empty string.
Notes:
the input will always be valid;
treat letters as case-insensitive
Examples
"This is a test sentence."  ==>  "1a1c4e1h2i2n4s4t"
""                          ==>  ""
"555"                       ==>  ""
'''
def string_letter_count(s):
    s = s.lower()
    if s == '':
        return ''
    dict = {}
    if (s[0] >= 'a' and  s[0] <= 'z'):
        dict[s[0]] = 1
    for char in s[1:]:
        if char in dict:
            dict[char] += 1
        elif not(char >= 'a' and  char <= 'z'):
            pass
        else:
            dict[char] = 1
    string = ''
    for key in sorted(dict.keys()):
        string += str(dict[key])
        string += key
    return string


print(string_letter_count("This is a test sentence."));
print(string_letter_count("Take an input string and return a string that is made up of the number of occurences of each english letter in the input followed by that letter, sorted alphabetically. The output string shouldn't contain chars missing from input (chars with 0 occurence); leave them out. An empty string, or one with no letters, should return an empty string."));
