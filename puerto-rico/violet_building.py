#!/usr/bin/env python

import building

class VioletBuilding( building.Building ):
    occupied = False

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

class Hospice( SmallVioletBuilding ):
    name = 'Hospice'
    cost = 4
    points = 2
    desc = '+1 colonist for settling (Settler phase)'

class Office( SmallVioletBuilding ):
    name = 'Office'
    cost = 5
    points = 2
    desc = 'Sell same kind of good (Trader phase)'

class LargeMarket( SmallVioletBuilding ):
    name = 'Large Market'
    cost = 5
    points = 2
    desc = '+2 doubloons with sale (Trader phase)'

class LargeWarehouse( SmallVioletBuilding ):
    name = 'Large Warehouse'
    cost = 6
    points = 2
    desc = 'Store 2 kinds of goods (Captain phase)'

class Factory( SmallVioletBuilding ):
    name = 'Factory'
    cost = 7
    points = 3
    desc = '+0/1/2/3/5 doubloons with production (Craftsman phase)'

class University( SmallVioletBuilding ):
    name = 'University'
    cost = 8
    points = 3
    desc = '+1 colonist for building (Builder phase)'

class Harbor( SmallVioletBuilding ):
    name = 'Harbor'
    cost = 8
    points = 3
    desc = '+1 victory point per delivery (Captain phase)'

class Wharf( SmallVioletBuilding ):
    name = 'Wharf'
    cost = 9
    points = 3
    desc = 'Your own ship (Captain phase)'

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


