import random
with open('sowpods.txt') as f:
	words = list(f)
guess_word = random.choice(words).strip()
print(guess_word)

guess = [ ]
guess_str = ' '
letter_count = 0
count_each_letter = 0
while letter_count < len(guess_word):
    guess_character = input('please guess a character: ')
    if guess_character != guess_word[letter_count]:
        print('incorrect')
        count_each_letter += 1
        if count_each_letter >= 6:
            print('you hang, lost')
        break
    else:
        guess.append(guess_character)
        print('you guessed just right: ' + guess_str.join(guess))
        letter_count += 1
