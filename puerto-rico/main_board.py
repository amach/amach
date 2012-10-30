#!/usr/bin/env python

import building

# Generates the main board with appropriate building amounts
class Board( object ):
    def __init__( self, num_players ):
        self.num_players = num_players

        self.prod_buildings = set([
            building.Guild(), building.Guild(), building.Guild(), building.Guild(),
            building.Res(), building.Res()
        ])

        self.plant_buildings = set([
            building.SmallIndigo(), building.SmallIndigo(), building.SmallIndigo(), building.SmallIndigo(),
            building.Indigo(), building.Indigo(),
            building.Tobacco(), building.Tobacco()
        ])

    def print_buildings( self ):
        print 'Violet Building (Cost, Victory Points):'

        for build in self.prod_buildings:
            print build.name +  ' (' + str(build.cost) + ', ' + str(build.points) + ')'

        print ''
        print 'Production Building (Cost, Victory Points, Storage Capacity)'

        for build in self.plant_buildings:
            print build.name + ' (' + str(build.cost) + ', ' + str(build.points) + ', ' \
                    + str(build.storage) + ')'

