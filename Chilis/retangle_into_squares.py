"""The drawing below gives an idea of how to cut a given "true" rectangle into squares ("true" rectangle meaning that the two dimensions are different).

alternative text

Can you translate this drawing into an algorithm?

You will be given two dimensions

a positive integer length (parameter named lng)
a positive integer width (parameter named wdth)
You will return an array or a string (depending on the language; Shell bash, PowerShell and Fortran return a string) with the size of each of the squares.

  sqInRect(5, 3) should return [3, 2, 1, 1]
  sqInRect(3, 5) should return [3, 2, 1, 1]

  Your result and the reference test solution are compared by strings.
"""
# recursive solution


def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    list = []
    if wdth == 1:
        for i in range(lng):
            list.append(1)
    else:
        n1 = lng // wdth
        for i in range(n1):
            list.append(wdth)
        # The next two lines of code do all the transition to next round
        lng1 = wdth
        wdth1 = lng - n1*wdth
        if wdth1 != 0:
            list += sqInRect(lng1, wdth1)
    return list


print(sqInRect(25, 3))
