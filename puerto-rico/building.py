#!/usr/bin/env python

class Building( object ):
    pass

class VioletBuilding( Building ):
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

class SmallSugar( Plant ):
    name = 'SmallSugar'
    cost = 2
    points = 1
    storage = 1

class Sugar( Plant ):
    name = 'Sugar'
    cost = 4
    points = 2
    storage = 3

class Coffee( Plant ):
    name = 'Coffee'
    cost = 6
    points = 3
    storage = 2
