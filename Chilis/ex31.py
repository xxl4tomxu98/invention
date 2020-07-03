clue_word = 'evaporate'

guess = [ ]
guess_str = ''
count = 0
while count < len(clue_word):
    guess_character = input('please guess a character: ')
    if guess_character != clue_word[count]:
        print('incorrect')
    else:
        guess.append(guess_character)
        print('you guessed just right: ' + guess_str.join(guess))
        count += 1
print('congratulation, you got right the whole word')