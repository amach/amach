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
        if self.cur_buildings < self.max_buildings:
            if self.num_coins > building.cost:
                self.buildings.append(building)
                self.cur_buildings += 1

                # if university is equipped, equip the building
            else:
                print 'Not enough money'
        else:
            print 'Max buildings' # check if this ever happens before game ends

    def buy_plant( self, plant ):
        if self.cur_plants < self.max_plants:
            if self.num_coins > plant.cost:
                self.plants.append(plant)
                self.cur_plants += 1

                # if hospice is owned + equipped, equip the plant
            else:
                print 'Not enough money'
        else:
            print 'Max plants'

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
            print r, self.resources[r]

