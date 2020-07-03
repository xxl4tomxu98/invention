import random
d1 = {}
for i in range(10000):
    x = random.randrange(10) 
    d1[x] = d1.get(x, 0) + 1
d2 = {}
for i in range(10000):
    x = int(random.random()*10)
    d2[x] = d2.get(x, 0) + 1
#note randint(a,b) should include b value, not random(a,b) or randrange(a,b) 
d3 = {}
for i in range(10000):
    x = random.randint(0, 10)
    d3[x] = d3.get(x, 0) + 1


# now let us see how to judge stochastic or deterministic
mylist = []

for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
print(mylist)

#turn this into deterministic
mylist1 = []

for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        if number not in mylist:
            mylist1.append(number)
print(mylist1)

mylist2 = []

random.seed(0)
for i in range(random.randint(1, 10)):
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist2.append(number)
    print(mylist2)
    
random.seed(9001)
random.randint(1, 10)

random.seed(9001)
for i in range(random.randint(1, 10)):
    print(random.randint(1, 10))
    
random.seed(9001)
d = random.randint(1, 10)
for i in range(random.randint(1, 10)):
    print(d)

random.seed(9001)
d = random.randint(1, 10)
for i in range(random.randint(1, 10)):
    if random.randint(1, 10) < 7:
        print(d)
    else:
        random.seed(9001)
        d = random.randint(1, 10)
        print(random.randint(1, 10))