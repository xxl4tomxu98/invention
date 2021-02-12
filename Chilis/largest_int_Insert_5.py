# Sequence method where each digit is checked to decide where
# insertion will be made
def solution(n: int, target_num: int = 5):
    target_digit = str(target_num)
    digits = str(n)
    if n >= 0:
        mod, result, checked_digits = (1, [], digits)
    else:
        mod, result, checked_digits = (-1, ['-'], digits[1:])
    for i, digit in enumerate(checked_digits):
        if int(digit) * mod < target_num * mod:
            result.append(target_digit)
            result.append(checked_digits[i:])
            break
        else:
            result.append(digit)
            if i == len(checked_digits) - 1:
                result.append(target_digit)
    return int("".join(result))


# Insertion method, where each insertion is compared
def solve(n, digit_num):
    temp = str(n)
    ans = float('-inf')
    for i in range(len(temp) + 1):
        cand = temp[:i] + str(digit_num) + temp[i:]
        if i == 0 and temp[0] == '-':
            continue
        ans = max(ans, int(cand))
    return ans


print(solution(-5530, 5))
print(solve(-55320, 5))
