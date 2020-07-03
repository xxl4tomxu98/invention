import random
#a = random.sample(range(1, 30), 12)
#b = random.sample(range(1, 30), 16)
a = [1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c =[x for x in set(b) if x in a]


print(c)
