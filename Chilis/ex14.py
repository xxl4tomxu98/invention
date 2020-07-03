a = [1, 1, 2, 3, 5, 8, 13, 21, 1, 34, 55, 89, 5]
b = []
i = 0
while i < len(a):
    if a[i] not in b:
        b.append(a[i])
    else:
        pass

    i += 1

print(b)



def remove_dup(lista):
    c = []
    for i in lista:
        if i in c:
            pass
        else:
            c.append(i)
    return c
print(remove_dup(a))
