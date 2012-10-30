#!/usr/bin/env python

class Role( object ):
    pass

class Settler( Role ):
    name = 'Settler'

class Mayor( Role ):
    name = 'Mayor'

class Builder( Role ):
    name = 'Builder'

class Craftsman( Role ):
    name = 'Craftsman'

class Trader( Role ):
    name = 'Trader'

class Captain( Role ):
    name = 'Captain'

class Prospector( Role ):
    name = 'Prospector'

class Game( object ):
    
    def __init__( self, num_players ):
        self.coins1 = 46
        self.coins5 = 8
        self.points1 = 32
        self.points5 = 18

        self.roles = [Settler(), Mayor(), Builder(), Craftsman(),
                Trader(), Captain()]

        if num_players == 3:
            self.start_coins = 2
            self.total_points = 75
            self.points1 = 20
            self.points5 = 11
            self.colonists = 55
            self.cargo_ship1 = 4
            self.cargo_ship2 = 5
            self.cargo_ship3 = 6
        elif num_players == 4:
            self.start_coins = 3
            self.total_points = 100
            self.points1 = 25
            self.points5 = 15
            self.colonists = 75
            self.cargo_ship1 = 5
            self.cargo_ship2 = 6
            self.cargo_ship3 = 7
            self.roles.append(Prospector())
        elif num_players == 5:
            self.start_coins = 4
            self.total_points = 122
            self.colonists = 95
            self.cargo_ship1 = 6
            self.cargo_ship2 = 7
            self.cargo_ship3 = 8
            self.roles.append(Prospector())
            self.roles.append(Prospector())
        else:
            print 'invalid number of players'
            exit(1)

        self.roles = set(self.roles)
        self.face_up_plants = num_players + 1
        self.col_ship = num_players

        self.coins1 = self.coins1 - (num_players * self.start_coins)

        
    def print_stats( self ):
        print 'Coins (1, 5): ' + str(self.coins1) + ', ' + str(self.coins5)
        print 'Starting Coins: ' + str(self.start_coins)
        print 'Colonists: ' + str(self.colonists)
        print 'Colonist Ship: ' + str(self.col_ship)
        print 'Cargo Ship 1: ' + str(self.cargo_ship1)
        print 'Cargo Ship 2: ' + str(self.cargo_ship2)
        print 'Cargo Ship 3: ' + str(self.cargo_ship3)
        print 'Points (1, 5): ' + str(self.points1) + ', ' + str(self.points5)
        print 'Total Points: ' + str(self.total_points)
        print 'Face-up plants: ' + str(self.face_up_plants)

        print 'Roles:'
        for role in self.roles:
            print role.name
