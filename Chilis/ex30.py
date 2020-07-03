import random
def random_word():
    word_list = []
    count = 0
    guess = ' '
    with open('sowpods.txt', 'r') as open_file:
        word = open_file.readline().strip()
        word_list.append(word)
        while word:
            count += 1
            word = open_file.readline().strip()
            word_list.append(word)
    guess = random.choice(word_list)
    print(word_list)
    return guess

print(random_word())


words = []
with open('sowpods.txt', 'r') as f:
    line = f.readline().strip()
    words.append(line)
    while line:
      line = f.readline().strip()
      words.append(line)

  # generate a random number
random_index = random.randint(0, len(words))

  # take the word
print("Random word: ", words[random_index])


with open('sowpods.txt') as f:
	words = list(f)
print(random.choice(words).strip())