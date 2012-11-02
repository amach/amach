#!/usr/bin/env python

import main_game
#import main_board

def main():
    players = int(raw_input('How many players? '))
    game = main_game.Game(players)
#    board = main_board.Board(players)
#    print ''
#    print 'Game stats:'
#    game.print_stats()
#    print ''
#    print 'Game board:'
#    board.print_buildings()
#
#    for p in range(1, players+1):
#        print 'Player {0}\'s board'.format(p)

if __name__ == '__main__':
    main()
