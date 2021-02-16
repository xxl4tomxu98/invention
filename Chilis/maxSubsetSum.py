"""If you are confused about why we need to track the max value found so far,
consider the following 3 cases instead:

only current number is selected, it is a[i]
current number is selected, it is dp[i-2] + arr[i]
current number is not selected, it is dp[i-1]
The value for current position is the maxiumum value of the above 3 cases."""


def maxSubsetSum(arr):
    dp = {}  # key : max index of subarray, value = sum
    dp[0], dp[1] = arr[0], max(arr[0], arr[1])
    for i, num in enumerate(arr[2:], start=2):
        dp[i] = max(dp[i-1], dp[i-2]+num, dp[i-2], num)
    return dp[len(arr)-1]


def maxSubsetSum1(arr):
    dp = []
    dp.append(arr[0])
    dp.append(max(arr[:2]))
    ans = max(dp)
    for a in arr[2:]:
        dp.append(max(max(dp[-2]+a, a), ans))
        ans = max(ans, dp[-1])
    return ans


def maxSubsetSum2(arr):
    dp = []
    dp.append(arr[0])
    dp.append(max(arr[:2]))
    for a in arr[2:]:
        dp.append(max([
            dp[-2]+a,
            a,
            dp[-1]
        ]))
    return dp[-1]


# recursive
def maxSubsetSum3(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr)
    return max([
        arr[0],
        arr[0] + maxSubsetSum3(arr[2:]),
        maxSubsetSum3(arr[1:])
    ])


def maxSubsetSum4(arr):
    maxSoFar = [arr[0], max(arr[:2])]
    for i, x in enumerate(arr[2:], 2):
        maxSoFar[i % 2] = max(x, maxSoFar[(i-1) % 2], maxSoFar[i % 2]+x)
    return max(maxSoFar + [0])


def maxSubsetSum5(arr):
    incl = max(arr[0], arr[1], 0)
    excl = max(arr[0], 0)
    for i in range(2, len(arr)):
        incl, excl = max(incl, excl + arr[i]), incl
    return incl


if __name__ == '__main__':
    print(maxSubsetSum1([-12, -23, -43, -45, -45, -133, 0, 23]))
    print(maxSubsetSum2([-12, -23, -43, -45, -45, -133, 0, 23]))
    print(maxSubsetSum3([-12, -23, -43, -45, -45, -133, 0, 23]))
    print(maxSubsetSum4([-12, -23, -43, -45, -45, -133, 0, 23]))
    print(maxSubsetSum5([-12, -23, -43, -45, -45, -133, 0, 23]))
    print(maxSubsetSum([-12, -23, -43, -45, -45, -133, 0, 23]))
