"""If we list all the natural numbers below 10 (inclusive of 1 and n,
or any (m, n+1) ranges) that are multiples of 3 or 5,
we get 1(3^0*5^0), 3(3^1*5^0), 5(3^0* 5^1), 9(3^2*5^0) .
The sum of number of these multiples is 4. Please note that ideal numbers
are those combinations of int powers to 3 or 5. Not just divisible by them.
Find the sum of all the multiples of 3 or 5 below but includes n."""


import math


def num_ideal_nums(m, n):
    all_powers = set([1])  # add 1 as a special case

    # find all powers smaller or equal to n and greater or equal to m

    for i in range(0, math.ceil(math.log(n, 3))):
        for j in range(0, math.ceil(math.log(n, 5))):
            if pow(3, i)*pow(5, j) <= n and pow(3, i)*pow(5, j) >= m:
                all_powers.add(pow(3, i))
                all_powers.add(pow(5, j))

    print(all_powers)

    return len(all_powers)


print(num_ideal_nums(1, 10))
print(num_ideal_nums(100, 1000))
