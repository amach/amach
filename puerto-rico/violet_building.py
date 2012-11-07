#!/usr/bin/env python

import building

class VioletBuilding( building.Building ):
    pass

class SmallVioletBuilding( VioletBuilding ):
    pass

class BigVioletBuilding( VioletBuilding ):
    pass

class SmallMarket( SmallVioletBuilding ):
    name = 'Small Market'
    cost = 1
    points = 1
    desc = '+1 coin when selling a good (Trader phase)'

class Hacienda( SmallVioletBuilding ):
    name = 'Hacienda'
    cost = 2
    points = 1
    desc = '+1 plantation from supply (Settler phase)'

class ConstructionHut( SmallVioletBuilding ):
    name = 'Construction Hut'
    cost = 2
    points = 1
    desc = 'May take a quarry instead of a plantation (Settler phase)'

class SmallWarehouse( SmallVioletBuilding ):
    name = 'Small Warehouse'
    cost = 3
    points = 1
    desc = 'Store 1 kind of remaining good instead of spoiling (Captain phase)'

class GuildHall( BigVioletBuilding ):
    name = 'Guild Hall'
    cost = 10
    points = 4

class Residence( BigVioletBuilding ):
    name = 'Residence'
    cost = 10
    points = 4

class Fortress( BigVioletBuilding ):
    name = 'Fortress'
    cost = 10
    points = 4

class CustomsHouse( BigVioletBuilding ):
    name = 'Customs House'
    cost = 10
    points = 4

class CityHall( BigVioletBuilding ):
    name = 'City Hall'
    cost = 10
    points = 4


