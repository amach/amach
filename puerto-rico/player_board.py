#!/usr/bin/env python

class Resource( object ):
    pass

class Corn( ResourceType ):
    name = 'Corn'
    value = 0

class Indigo( ResourceType ):
    name = 'Indigo'
    value = 1

class Sugar( ResourceType ):
    name = 'Sugar'
    value = 2

class Tobacco( ResourceType ):
    name = 'Tobacco'
    value = 3

class Coffee( ResourceType ):
    name = 'Coffee'
    value = 4

class PlayerBoard( object ):

    def __init__( self, num_coins ):
        corn = Corn()
        indigo = Indigo()
        sugar = Sugar()
        tobacco = Tobacco()
        coffee = Coffee()

        self.num_coins = num_coins
        self.max_plants = 12
        self.cur_plants = 0
        self.max_buildings = 12
        self.cur_buildings = 0
        self.resources = {
            corn: 0,
            indigo: 0,
            sugar: 0,
            tobacco: 0,
            coffee: 0
            }

    def print_board( self ):
        print 'Player board:'
        print 'Coins: {0}'.format(self.num_coins)
        print 'Plants (current/max): {0}/{1}'.format(self.cur_plants, self.max_plants) 
        print 'Buildings (current/max): {0}/{1}'.format(self.cur_buildings, self.max_buildings)
        print 'Resources:'
        for r in self.resources:
            print r.name, self.resources[r]
