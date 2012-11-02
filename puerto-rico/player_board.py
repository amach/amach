#!/usr/bin/env python

import resource

class PlayerBoard( object ):

    def __init__( self, num_coins ):
        corn = resource.Corn()
        indigo = resource.Indigo()
        sugar = resource.Sugar()
        tobacco = resource.Tobacco()
        coffee = resource.Coffee()

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
