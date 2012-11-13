#!/usr/bin/env python

import sys
import main_game

def main():
    try:
        players = int(raw_input('How many players? '))
        game = main_game.Game(players)
        game.select_role()
    except Exception, ex:
        print 'Quitting because of fatal error:', ex
        sys.exit(1)

if __name__ == '__main__':
    main()
