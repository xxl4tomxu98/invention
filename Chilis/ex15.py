test_string = 'we will overcome, we will overcome, we will overcome someday. '
result = test_string.split()
print(result)
reverse_arr = result[::-1]

print(reverse_arr)


def reversal_word(w):
    return ' '.join(w.split()[::-1])


print(reversal_word(test_string))
