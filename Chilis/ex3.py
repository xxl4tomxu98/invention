a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
d = []
for x in a:
    if x < 5:
        d.append(x)
print(d)

b = list(filter(lambda y: y < 5, a))
print(b)

c = [z for z in a if z < 5]
print(c)