a = int(input('please input integer a: '))
b = int(input('please input integer b: '))
c = int(input('please input integer c: '))

if a > b and a > c:
    print('a is the largest')
elif b < c and a < c:
    print('c is the largest')
elif b > a and b > c:
    print('b is the largest')
else:
    print('no single largest')



def max_of_3(a, b, c):
    max_3 = 0
    if a > b:
        if a > c:
            max_3 = a
        else:
            max_3 = c
    else:
        if c < b:
            max_3 = b
        else:
            max_3 = c
    return max_3

print(max_of_3(12, 23, 33))
