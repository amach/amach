#!/usr/bin/env python

class Role( object ):
    pass

class Settler( Role ):
    name = 'Settler'
    desc = 'Action: Each player takes and places a plantation tile. \
        Privilege: The Settler may take and place a quarry instead of a plantation.'

class Mayor( Role ):
    name = 'Mayor'
    desc = 'Action: Each player takes and places colonists. \
            Privilege: The Mayor may take an additional colonist.'

class Builder( Role ):
    name = 'Builder'
    desc = 'Action: Each player may build a building. \
            Privilege: The Builder pays one less coin.'

class Craftsman( Role ):
    name = 'Craftsman'
    desc = 'Action: All players take goods from the supply. \
            Privilege: The Craftsman takes an additional good.'

class Trader( Role ):
    name = 'Trader'
    desc = 'Action: Each player may, at most, sell 1 good to the trading house. \
            Privilege: The Trader earns 1 extra coni when he sells.'

class Captain( Role ):
    name = 'Captain'
    desc = 'Action: The players MUST load goods onto the cargo ships. \
            Privilege: The Captain earns 1 extra victory point.'

class Prospector( Role ):
    name = 'Prospector'
    desc = 'Action: none. \
            Privilege: The Prospector takes 1 coin from the bank.'
