num = int(input('please enter a number: '))
divisors = list(x for x in range(1, num + 1) if num % x == 0)
print(divisors)