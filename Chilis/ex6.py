str1 = input('please provide a string: ')
str1 = str1.replace(' ','')
if str1[::1] == str1[::-1]:
    print('str1 is palindrome')
else:
    print('str1 is not palindrome')