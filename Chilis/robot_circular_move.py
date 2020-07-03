# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 19:11:36 2020

@author: 13305
"""
# check if given set of moves is circular on not


def checkCircularMove(str):

    # start from coordinates (0, 0)
    x = y = 0

    # assume initial direction is North
    dir = 'N'

    # read each instruction from input String
    for c in str:
        # move one unit in same direction
        if c == 'M':
            if dir == 'N':
                y = y + 1
            elif dir == 'S':
                y = y - 1
            elif dir == 'E':
                x = x + 1
            elif dir == 'W':
                x = x - 1

        # change direction to left of current direction
        if c == 'L':
            if dir == 'N':
                dir = 'W'
            elif dir == 'W':
                dir = 'S'
            elif dir == 'S':
                dir = 'E'
            elif dir == 'E':
                dir = 'N'

        # change direction to right of current direction
        if c == 'R':
            if dir == 'N':
                dir = 'E'
            elif dir == 'E':
                dir = 'S'
            elif dir == 'S':
                dir = 'W'
            elif dir == 'W':
                dir = 'N'

    # if we're back to starting coordinates (0, 0),
    # the move is circular
    return x == 0 and y == 0


if __name__ == '__main__':

    str = "MMRMMRMMRMM"

    if checkCircularMove(str):
        print("Circular Move")
    else:
        print("Non-Circular Move")

    string = 'RRMMLLMMM'
    print(checkCircularMove(string))
