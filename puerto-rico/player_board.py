#!/usr/bin/env python

import resource
import building

class PlayerBoard( object ):

    def __init__( self, num_coins ):
        self.num_coins = num_coins
        self.num_points = 0
        self.max_plants = 12
        self.cur_plants = 0
        self.plants = set([]) 
        self.max_buildings = 12
        self.cur_buildings = 0
        self.buildings = set([])
        self.resources = {
            'Corn': 0,
            'Indigo': 0,
            'Sugar': 0,
            'Tobacco': 0,
            'Coffee': 0
            }

    def buy_building( self, building ):
        self.buildings.append(building)

    def buy_plant( self, plant ):
        self.plants.append(plant)

    def produce_resources( self, resource_type, num ):
        for r in self.resources:
            resources[resource_type] += num
            # need to check if players can have max number of a resource
    
    # default num=1 for selling resources, num can be set for shipping
    def remove_resources( self, resource_type, num=1 ):
        self.resources[resource_type] -= num

    def print_board( self ):
        print 'Player board:'
        print 'Coins: {0}'.format(self.num_coins)
        print 'Plants (current/max): {0}/{1}'.format(self.cur_plants, self.max_plants) 
        print 'Buildings (current/max): {0}/{1}'.format(self.cur_buildings, self.max_buildings)
        print 'Resources:'
        for r in self.resources:
            print r.name, self.resources[r]

