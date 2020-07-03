import numpy
game = [[1, 2, 0], [2, 1, 0], [2, 2, 1]]


def diagonal_win(game):
    # note that checking cells already put in pieces is essential it can either be 1 or 2
    if game[1][1] != 0 and game[1][1] == game[0][0] == game[2][2]:
        return game[1][1]
    elif game[1][1] != 0 and game[1][1] == game[0][2] == game[2][0]:
        return game[1][1]
    else:
        return 0


def line_win(game):
    for i in range(int(len(game))):
        # length of a set equal to 1 means all three are equal
        if len(set(game[i])) == 1 and game[i][0] != 0:
            return game[i][0]
    return 0


if line_win(game) > 0:
    print(str(line_win(game)) + str(" row wins!"))
if line_win(numpy.transpose(game)) > 0:
    print(str(line_win(numpy.transpose(game))) + str(" column wins!"))
if diagonal_win(game) > 0:
    print(str(diagonal_win(game)) + str(" diagonal wins!"))
