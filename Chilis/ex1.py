import datetime
now = datetime.datetime.now()
print('this is ' + str(now.year))
name = input('what is your name: ')
print('your name is ' + name)
age = input('how old are you: ')
print('your age is: ' + age)
turn_100 = now.year - int(age) + 100
num_copy = int(input('please give a number of copies desired: '))
while num_copy > 0:
    print(name + ' you will reach 100 yrs old in the year: ' + str(turn_100))
    num_copy = num_copy - 1
  