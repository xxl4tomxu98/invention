text = 'This is my test text, we keep text short to keep it manageable'

text = text.lower()

skips = ['.', ',', ';', ':', '"', "'"]

for char in skips:
    text = text.replace(char, '')
    

def count_words(text):
    word_count = {}
    counter = 0
    for word in text.split(' '):
        if word in list(word_count.keys()):
            counter += 1
        else:
            counter = 1    
        word_count.update({word:counter})
    return word_count


def count_words1(text):
    word_count = {}
    #counter = 0
    for word in text.split(' '):
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1    
    return word_count

count_words(text)

count_words1(text)



from collections import Counter


def count_words_fast(text):
    text = text.lower()

    skips = ['.', ',', ';', ':', '"', "'"]

    for char in skips:
        text = text.replace(char, '')
      
    word_counts = Counter(text.split(' '))
    return word_counts


def read_book(title_path): 
    """ this func read a book and return it as a string with '\n' and '\r' removed"""
    with open(title_path, 'r', encoding ='UTF8') as current_file:
        text = current_file.read()
        item_remove = ['\n', '\r']
        for char in item_remove:
            text = text.replace(char, '')
    return text    
    

def word_stats(word_counts):
    """return the number of unique words and word frequencies"""
    num_unique = len(word_counts)
    counts = word_counts.values()
    return(num_unique, counts)

text = read_book('./Books/English/shakespeare/Romeo and Juliet.txt')
word_counts = count_words_fast(text)
(num_unique, counts) = word_stats(word_counts)

print(num_unique, sum(counts))

text = read_book('./Books/German/shakespeare/Romeo und Julia.txt')
word_counts = count_words_fast(text)
(num_unique, counts) = word_stats(word_counts)   
print(num_unique, sum(counts))


import os
book_dir = './Books'


import pandas as pd
stats = pd.DataFrame(columns = ('language', 'author', 'title', 'length', 'unique'))
title_num = 1


for language in os.listdir(book_dir):
    for auhtor in os.listdir(book_dir + '/' + language):
        for title in os.listdir(book_dir + '/' + language + '/' + author):
            inputfile = book_dir + '/' + language + '/' + author + '/' + title 
            text = read_book(inputfile)
            (num_unique,counts) = word_stats(count_words_fast(text))
            stats.loc[title_num] = language, author.capitalize(), title.replace('.txt', ''), sum(counts), num_unique 
            title_num += 1

print(stats)
print(stats.top())
print(stats.tail())            
    
from matplotlib import pyplot as plt
plt.plot(stats.length, stats.unique, 'bo')
plt.loglog(stats.length, stats.unique, 'bo')

print(stats[stats.language == 'English'])

plt.figure(figsize = (10, 10))
subset = stats[stats.language == 'English']
plt.loglog(subset.length, subset.unique, 'o', label = 'English', color = 'crimson')
plt.loglog(subset.length, subset.unique, 'o', label = 'French', color = 'forestgreen')
plt.loglog(subset.length, subset.unique, 'o', label = 'German', color = 'orange')
plt.loglog(subset.length, subset.unique, 'o', label = 'Portuguese', color = 'blueviolet')
plt.legend()
plt.xlabel('Book Length')
plt.ylabel('Number of Unique Words ')
plt.savefig('language_plot.pdf')


        