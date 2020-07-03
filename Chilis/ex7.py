a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(list(filter(lambda x: a.index(x) % 2 == 1, a)))

b = [element for element in a if element % 2 == 0]
print(b)

c = a[::-2]
c.sort()
print(c)