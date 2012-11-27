#!/usr/bin/env python

import building

class PlantStorageStorage( building.Building ):
    occupied = 0

class SmallIndigo( PlantStorage ):
    name = 'SmallIndigo'
    cost = 1
    points = 1
    storage = 1

class Indigo( PlantStorage ):
    name = 'Indigo'
    cost = 3
    points = 2
    storage = 3

class Tobacco( PlantStorage ):
    name = 'Tobacco'
    cost = 5
    points = 3
    storage = 3

class SmallSugar( PlantStorage ):
    name = 'SmallSugar'
    cost = 2
    points = 1
    storage = 1

class Sugar( PlantStorage ):
    name = 'Sugar'
    cost = 4
    points = 2
    storage = 3

class Coffee( PlantStorage ):
    name = 'Coffee'
    cost = 6
    points = 3
    storage = 2
