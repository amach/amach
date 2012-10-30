#!/usr/bin/env python

class Game( object ):
    
    def __init__( self, num_players ):
        self.coins1 = 46
        self.coins5 = 8
        self.points1 = 32
        self.points5 = 18
        
        # to-do: cargo ship

        if num_players == 3:
            self.start_coins = 2
            self.total_points = 75
            self.points1 = 20
            self.points5 = 11
            self.colonists = 55
        elif num_players == 4:
            self.start_coins = 3
            self.total_points = 100
            self.points1 = 25
            self.points5 = 15
            self.colonists = 75
        elif num_players == 5:
            self.start_coins = 4
            self.total_points = 122
            self.colonists = 95
        else:
            print 'invalid number of players'
            exit(1)

        self.face_up_plants = num_players + 1
        self.col_ship = num_players

        self.coins1 = self.coins1 - (num_players * self.start_coins)

        # to-do: create role cards
        # 1 each of: settler, mayor, builder, craftsman, trader, captain
        # 0-2 prospectors for 3-5 players

    def print_stats( self ):
        print 'Coins (1, 5): ' + str(self.coins1) + ', ' + str(self.coins5)
        print 'Starting Coins: ' + str(self.start_coins)
        print 'Colonists: ' + str(self.colonists)
        print 'Colonist Ship: ' + str(self.col_ship)
        #print 'Cargo Ship: ' + str(self.cargo_ship)
        print 'Points (1, 5): ' + str(self.points1) + ', ' + str(self.points5)
        print 'Total Points: ' + str(self.total_points)
        print 'Face-up plants: ' + str(self.face_up_plants)
