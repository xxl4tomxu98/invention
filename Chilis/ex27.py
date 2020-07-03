game = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(3):
    for j in range(3):

        while game[i][j] == 0:
            move1 = input('player 1 please enter your move in (i,j) format: ')
            move1_list = move1.split(',')
            print(move1_list)
            game[int(move1_list[0])-1][int(move1_list[1])-1] = 1
            print(game)

            move2 = input('player 2 please enter your move in (i,j) format: ')
            move2_list = move2.split(',')
            print(move2_list)
            game[int(move2_list[0]) - 1][int(move2_list[1]) - 1] = 2
            print(game)

print('game over')

import numpy as np

game = np.zeros(9).reshape(3,3).astype('object')
print(game)

count = 1
player = 'player1'

while count < 10:
    x = input('What is your move %s? (mention the row, col position)' %player)
    x = x.strip().split(',')
    r = int(x[0])
    c = int(x[1])
    if game[r-1][c-1] == 0 and count%2 != 0:
        game[r-1][c-1] = 'x'
        player = 'player2'
    elif game[r-1][c-1] == 0 and count%2 == 0:
        game[r-1][c-1] = 'o'
        player = 'player1'
    else:
        print('invalid position')

    count += 1
    print(game)