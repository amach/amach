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


