#!/usr/bin/env python

import violet_building
import plant_storage

# Generates the main board with appropriate building amounts
class Board( object ):
    def __init__( self, num_players ):
        self.num_players = num_players

        self.prod_buildings = set([
            violet_building.GuildHall(), violet_building.GuildHall(), violet_building.GuildHall(), violet_building.GuildHall(),
            violet_building.Residence(), violet_building.Residence()
        ])

        self.plant_buildings = set([
            plant.SmallIndigo(), plant.SmallIndigo(), plant.SmallIndigo(), plant.SmallIndigo(),
            plant.Indigo(), plant.Indigo(),
            plant.Tobacco(), plant.Tobacco()
        ])

    def print_buildings( self ):
        print 'Violet Building (Cost, Victory Points):'

        for build in self.prod_buildings:
            print '{0} ({1}, {2})'.format(build.name, build.cost, build.points)

        print ''
        print 'Production Building (Cost, Victory Points, Storage Capacity)'

        for build in self.plant_buildings:
            print '{0} ({1}, {2}, {3})'.format(build.name, build.cost, build.points, 
                    build.storage)

