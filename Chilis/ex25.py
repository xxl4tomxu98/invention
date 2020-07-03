import math
allg = []

Value = int(input('I know the number is: '))

L, R = 0, 100
allg.append(math.floor((L+R)/2))

i = 0
while allg[i] != Value:

    if allg[i] < Value:
       print('Guess too low, guess again: ')
       L = allg[i]

    elif allg[i] > Value:
       print('Guess too high, guess again: ')
       R = allg[i]
    m = math.floor((L+R)/2)
    allg.append(m)
    print(allg)
    i += 1

print('you guess correctly!')
print('it took you ' + str(i + 1) + ' times to guess right.')

