'''Write a method, digitalRoot(num). It should sum the digits
of a positive integer. If it is greater than or equal to 10,
sum the digits of the resulting number. Keep repeating until
there is only one digit in the result, called the "digital root".
Do not use string conversion within your method.'''


def digitalRoot(num):
    while num > 10:
        num = sumDigits(num)
    return num


def sumDigits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum


print(digitalRoot(12348965))


def digital_root(num):
    # put digits into an array
    digits = []
    while num > 0:
        digits.append(num % 10)
        num = num // 10
    digit_sum = sum(digits)
    return digit_sum if digit_sum <= 10 else digital_root(digit_sum)


print(digital_root(12348965))


def digital_root2(num):
    return num if num <= 10 else digital_root2(
                  digital_root2(num // 10) + num % 10)


print(digital_root2(12348965))
