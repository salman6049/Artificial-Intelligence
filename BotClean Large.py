# -*- coding: utf-8 -*-
"""
Created October 2017

@author: Salman
"""

import math

def next_move(posx, posy, dimx, dimy, board):
    closest = [-1, -1, 25000, 8]
    for i in range(dimx):
        for j in range(dimy):
            if board[i][j] == 'd':
                neighbours = [[x, y] for x in range(dimx) for y in range(dimy) if abs(x - i) <= 1 and abs(y - j) <= 1 and board[x][y] == 'd']
                dist = abs(i - posx) + abs(j - posy)
                if dist < closest[2]:
                    closest = [i, j, dist, len(neighbours)]
                elif dist == closest[2]:
                    if len(neighbours) <= closest[3]:
                        closest = [i, j, dist, len(neighbours)]
    if closest[2] == 0:
        print('CLEAN')
    else:
        if abs(closest[0] - posx) > abs(closest[1] - posy):
            if closest[0] > posx:
                print('DOWN')
            else:
                print('UP')
        else:
            if closest[1] > posy:
                print('RIGHT')
            else:
                print('LEFT')

                
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)