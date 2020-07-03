# cow and bull game program
import string
import random
# def num_gen(size = 4, chars=string.digits):
#    return ''.join(random.choice(chars) for _ in range(size))
# print(num_gen(4))


if __name__ == '__main__':
    num_gen = str(random.randint(0, 9999))
    print('random number generated: ' + num_gen)
    user_guess = input('give me a guess of four digit number: ')
cow, bull = 0, 0
i = 0
while i in range(len(user_guess)):
    if user_guess[i] == num_gen[i]:
        cow += 1

    elif user_guess[i] in num_gen:
        bull += 1
    i += 1
print('you have ' + str(cow) + ' cows, and ' + str(bull) + ' bulls')
#    print(user_guess)
