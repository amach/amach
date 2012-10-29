#!/usr/bin/env python

class Building( object ):
    pass

class Guild( Building ):
    name = 'Guild'
    cost = 1
    points = 2

class Res( Building ):
    name = 'Res'
    cost = 2
    points = 4

class Plant( Building ):
    pass

class SmallIndigo( Plant ):
    name = 'SmallIndigo'
    cost = 1
    points = 1
    storage = 1

class Indigo( Plant ):
    name = 'Indigo'
    cost = 3
    points = 2
    storage = 3

class Tobacco( Plant ):
    name = 'Tobacco'
    cost = 5
    points = 3
    storage = 3

# Generates the main board with appropriate building amounts
class Board( object ):
    def __init__( self, num_players ):
        self.num_players = num_players

        self.prod_buildings = set([
            Guild(), Guild(), Guild(), Guild(),
            Res(), Res()
        ])

        self.plant_buildings = set([
            SmallIndigo(), SmallIndigo(), SmallIndigo(), SmallIndigo(),
            Indigo(), Indigo(),
            Tobacco(), Tobacco()
        ])

    def print_buildings( self ):
        print 'Violet Building (Cost, Victory Points):'

        for building in self.prod_buildings:
            print building.name +  ' (' + str(building.cost) + ', ' + str(building.points) + ')'

        print ''
        print 'Production Building (Cost, Victory Points, Storage Capacity)'

        for building in self.plant_buildings:
            print building.name + ' (' + str(building.cost) + ', ' + str(building.points) + ', ' \
                    + str(building.storage) + ')'

