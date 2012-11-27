#!/usr/bin/env python

import resource
import violet_building
import plant_storage

class PlayerBoard( object ):
    MAX_PLANTS = 12
    MAX_BUILDINGS = 12

    # TBD: how to allow for equipping/re-equipping plants?
    def __init__( self, num_coins ):
        self.num_coins1 = num_coins
        self.num_coins5 = 0
        self.coin_total = num_coins1
        self.num_points1 = 0
        self.num_points5 = 0
        self.point_total = 0
        self.cur_plants = 0
        self.plants = set([])
        self.cur_buildings = 0
        self.buildings = {}
        self.resources = {
            'Corn': 0,
            'Indigo': 0,
            'Sugar': 0,
            'Tobacco': 0,
            'Coffee': 0
            }

    def buy_building( self, building ):

        # check if player already has that building

        if self.cur_buildings < MAX_BUILDINGS:
            if self.num_coins > building.cost:

                # if university is owned + occupied, occupy the new building
                if 'University' in self.buildings and self.buildings['University'].occupied:
                    building.occupied = True

                self.buildings[building.name] = building
                self.cur_buildings += 1

                self.coin_total -= building.cost
                self.num_coins5 -= building.cost / 5
                self.num_coins1 -= building.cost % 5

            else:
                print 'Not enough money'
        else:
            print 'Max buildings' # check if this ever happens before game ends

    def add_plant( self, plant ):
        if self.cur_plants < MAX_PLANTS:

            # if hospice is owned + occupied, equip the plant
            if 'Hospice' in self.buildings and self.buildings['Hospice'].occupied:
                plant.occupied = 1
                    
            self.plants.append(plant)
            self.cur_plants += 1

        else:
            print 'Max plants'

    def produce_resources( self ):
        count_storage = self.buildings

        for p in self.plants:
            # todo: confirm if players can have max number of a resource
            if p.occupied:
                if p.name == 'Corn':
                    resources['Corn'] += 1
                elif p.name == 'Indigo':
                    if 'SmallIndigo' in self.buildings and count_storage['SmallIndigo'].occupied > 0:
                        count_storage['SmallIndigo'].occupied -= 1
                        resources['Indigo'] += 1
                    elif 'LargeIndigo' in self.buildings and count_storage['LargeIndigo'].occupied > 0:
                        count_storage['LargeIndigo'].occupied -= 1
                        resources['Indigo'] += 1

                elif p.name == 'Sugar':
                    if 'SmallSugar' in self.buildings and count_storage['SmallSugar'].occupied > 0:
                        count_storage['SmallSugar'].occupied -= 1
                        resources['Sugar'] += 1
                    elif 'LargeSugar' in self.buildings and count_storage['LargeSugar'].occupied > 0:
                        count_storage['LargeSugar'].occupied -= 1
                        resources['Sugar'] += 1

                elif p.name == 'Tobacco':
                    if 'Tobacco' in self.buildings and count_storage['Tobacco'].occupied > 0:
                        count_storage['Tobacco'].occupied -= 1
                        resources['Tobacco'] += 1

                elif p.name == 'Coffee':
                    if 'Coffee' in self.buildings and count_storage['Coffee'].occupied > 0:
                        count_storage['Coffee'].occupied -= 1
                        resources['Coffee'] += 1
                else:
                    print 'This should never happen'

    
    # default num=1 for selling resources, num can be set for shipping
    def remove_resources( self, resource_type, num=1 ):
        self.resources[resource_type] -= num

    def print_board( self ):
        print 'Player board:'
        print 'Coins: {0}'.format(self.num_coins)
        print 'Plants (current/max): {0}/{1}'.format(self.cur_plants, MAX_PLANTS) 
        print 'Buildings (current/max): {0}/{1}'.format(self.cur_buildings, MAX_BUILDINGS)
        print 'Resources:'
        for r in self.resources:
            print r, self.resources[r]

