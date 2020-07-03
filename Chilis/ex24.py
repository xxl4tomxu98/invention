def horizontal_bar():
    print(' - - - ' * size)
    return
# horizontal_bar()


def vertical_bar():
    print('|      ' * (size + 1))
    return

# vertical_bar()


# Drawing squared board for games
if __name__ == '__main__':
    size = int(input('please indicate what type of board: '))
    for i in range(size):
        horizontal_bar()
        vertical_bar()
    horizontal_bar()
