#!/usr/bin/env python

import building

class Plant( building.Building ):
    equipped = 0

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
