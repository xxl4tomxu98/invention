import random
a = random.randint(1, 9)
guess = 0
count = 0
while guess != a and guess != 'exit':
    guess = int(input('please guess a integer between 1 and 9: '))

    if guess == 'exit':
        break

    count += 1

    if guess < a:
        print('you guessed too low')
    elif guess > a:
        print('you guessed too high')
    else:
        print('you guessed just right!')
        print('and it only took you ', count, 'tries')