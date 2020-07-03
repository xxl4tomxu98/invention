import os

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    dict = {}
    for j in ar:
        if j in dict:
            dict[j] += 1
        else:
            dict[j] = 1
        res = 0
        for k, v in dict.items():
            res += v//2
        return res


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(str(result) + '\n')
