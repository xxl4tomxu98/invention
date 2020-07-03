num = int(input('please enter a number: '))
if num % 4 == 0:
    print('this number is a multiple of 4')
elif num % 2 == 0:
    print('this is an even number')
else:
    print ('this is an odd number')

check_num = int(input('enter a check number to see if ' + str(num) + ' is divisible by:'))
if num % check_num == 0:
    print('Yes, '+str(num)+' is divisible by '+str(check_num))
else:
    print('No, '+str(num)+' is not divisible by ' + str(check_num))

