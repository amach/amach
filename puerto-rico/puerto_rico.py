#!/usr/bin/env python

import main_game
import main_board

def main():
    players = int(raw_input('How many players? '))
    game = main_game.Game(players)
    board = main_board.Board(players)
    print ''
    print 'Game stats:'
    game.print_stats()
    print 'Game board:'
    board.print_buildings()

if __name__ == '__main__':
    main()
