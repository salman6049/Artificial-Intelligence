# -*- coding: utf-8 -*-
"""
Created on  July 25 00:50:20 2019

@author: Salman
"""

#!/bin/python

INITIAL_MONEY = 100
BOARD_SIZE    = 11

def calculate_bid(player, pos, first_moves, second_moves):

    def calculate(pos, moves, opponent_moves):
        money          = INITIAL_MONEY - sum(moves)
        opponent_money = INITIAL_MONEY - sum(opponent_moves)

        spots_remaining          = BOARD_SIZE - pos
        opponent_spots_remaining = BOARD_SIZE - spots_remaining

        winning  = spots_remaining < opponent_spots_remaining
        base_bid = (money / spots_remaining)

        if winning:
            # We'll try to make him waste his money, bwahah
            return base_bid
        else:
            # if money <= opponent_money:
                # We'll try the same strategy that he did to us
            return base_bid + 2

    if player == '1':
        return calculate(pos, first_moves, second_moves)
    else:
        return calculate(pos, second_moves, first_moves)


player     = input() # gets the id of the player
scotch_pos = input() # current position of the scotch

first_moves = [int(i) for i in raw_input().split()]
second_moves = [int(i) for i in raw_input().split()]
bid = calculate_bid(player,scotch_pos,first_moves,second_moves)
print bid