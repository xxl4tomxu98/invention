import string
import random

s = 'safwesjfkw74e8293!*^sjfdesklj&cdjskfq2432HJTY3)(*%$^'
passlen = 10
p = ''.join(random.sample(s,passlen))
print(p)

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))
print(pw_gen(int(input('How many characters in your password? '))))


password = ''
count = 0
length = int(input('how many characters would you like in your password? '))

while count != length:
    upper = [random.choice(string.ascii_uppercase)]
    lower = [random.choice(string.ascii_lowercase)]
    num = [random.choice(string.digits)]
    symbol = [random.choice(string.punctuation)]
    everything = upper + lower + num + symbol

    password += random.choice(everything)
    count += 1
    continue
if count == length:
    print(password)

