#!/usr/bin/env python

class Game( object ):
    coins1 = 46
    coins5 = 8
    points1 = 32
    points5 = 18
    
    def __init__( self, num_players ):
        
        if num_players == 3:
            self.start_coins = 2
            self.points = 75
            self.colonists = 55
        elif num_players == 4:
            self.start_coins = 3
            self.points = 100
            self.colonists = 75
        elif num_players == 5:
            self.start_coins = 4
            self.points = 122
            self.colonists = 95
        else:
            print 'invalid number of players'
            exit(1)

        self.face_up_plants = num_players + 1
        self.col_ship = num_players

        # to-do: create role cards
        # 1 each of: settler, mayor, builder, craftsman, trader, captain
        # 0-2 prospectors for 3-5 players
