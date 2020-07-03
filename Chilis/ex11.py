num = int(input('please enter a number: '))
divisors = list(x for x in range(1, num + 1) if num % x == 0)
if len(divisors) <= 2:  # only divisible by 1 and itself
    print('num is a prime number ')
else:
    print('num is not a prime number ')


import sys
number = int(input('please enter a number: '))
if number > 0:
    for x in range (2, number - 1): #this range excludes number and 1, both of which number is divisible by
        if number % x != 0: # If number isn't evenly divisible by x, start over with the next one
            continue
        elif number % x == 0: # If number is evenly divisible by x, it can't be prime
            sys.exit("The number is not prime.")
    sys.exit("The number is prime.") # number wasn't evenly divisible by any x, so it's prime
elif number == 0:
    sys.exit("The number is not prime.") #According to the Google, 0 is not prime
else:#if number is less than 0, the number is not prime (according to the Google).
    sys.exit("The number is not prime.")