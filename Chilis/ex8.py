player1 = input('player1 hand: ')
player2 = input('player2 hand: ')
while player1 == player2:
    print('tie, throw your hand again:')
    player1 = input('player1 hand: ')
    player2 = input('player2 hand: ')
    if player1 == 'quit' or player2 =='quit':
        break
if player1 == 'rock' and player2 =='scissor':
        print('player1 won, would you want another game?')
elif player1 == 'rock' and player2 =='paper':
        print('player2 won, would you want another game?')
elif player1 == 'scissor' and player2 =='paper':
        print('player1 won, would you want another game?')
elif player1 == 'scissor' and player2 =='rock':
        print('player2 won, would you want another game?')
elif player1 == 'paper' and player2 =='scissor':
        print('player2 won, would you want another game?')
elif player1 == 'paper' and player2 =='rock':
        print('player1 won, would you want another game?')

