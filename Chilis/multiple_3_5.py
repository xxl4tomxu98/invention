'''If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.'''


def multiples(n):
    count = 0
    sum = 0
    for i in range(n):
        if(i % 3 == 0) or (i % 5 == 0):
            count += 1
            sum += i
    return count, sum


# This is an elimination method where not divisible
# numbers are substracted from total range
def multiples1(n):
    return n - round(n*(2/3 * 4/5))


print(multiples(200))
print(multiples(10))
print(multiples1(200))
print(multiples1(10))
