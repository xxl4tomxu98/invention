def solution(A):
    # write your code in Python 3.6
    A.sort()
    if A[-1] <= 0 or A[0] > 1:
        return 1
    for n in range(1, A[-1]):
        if n not in A:
            return n
    return A[-1] + 1


print(solution([-230, -340, 0, 1, 3, 50, 90]))
