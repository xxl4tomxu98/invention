'''Write a function, fibsSum(n), that finds the sum of the first
n fibonacci numbers recursively. Assume n > 0. Note that for this
problem, the fibonacci sequence starts with [1, 1].'''


def fibSum(n):
    fibNum = 0
    for i in range(1, n+1):
        fibNum += fibonacci(i)
    return fibNum


def fibSumRecur(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fibSumRecur(n-1) + fibonacci(n)


def fibonacci(n, memo={}):
    if n == 1 or n == 2:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fibonacci(n-2) + fibonacci(n-1)
    return memo[n]


print(fibSum(7))
print(fibSumRecur(7))
