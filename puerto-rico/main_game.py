#!/usr/bin/env python

import random
import role
import main_board
import player_board
import resource

class Game( object ):
    
    def __init__( self, num_players ):
        
        # starting amounts of items
        self.coins1 = 46
        self.coins5 = 8
        self.num_quarry = 8
        self.num_coffee = 8
        self.num_tobacco = 9
        self.num_corn = 10
        self.num_sugar = 11
        self.num_indigo = 12
        self.face_up_plants = num_players + 1
        self.col_ship = num_players

        # base roles (prospectors added if needed)
        self.roles = [role.Settler(), role.Mayor(), role.Builder(), role.Craftsman(),
                role.Trader(), role.Captain()]

        self.plants = []
        self.player_boards = []

        # generate central game board (why is num_players required here?)
        self.board = main_board.Board(num_players)

        # set values which depend on number of players
        if num_players == 3:
            self.start_coins = 2
            self.total_points = 75
            self.points1 = 20
            self.points5 = 11
            self.colonists = 55
            self.cargo_ship1 = 4
            self.cargo_ship2 = 5
            self.cargo_ship3 = 6
        elif num_players == 4:
            self.start_coins = 3
            self.total_points = 100
            self.points1 = 25
            self.points5 = 15
            self.colonists = 75
            self.cargo_ship1 = 5
            self.cargo_ship2 = 6
            self.cargo_ship3 = 7
            self.roles.append(role.Prospector())
        elif num_players == 5:
            self.start_coins = 4
            self.total_points = 122
            self.points1 = 32
            self.points5 = 18
            self.colonists = 95
            self.cargo_ship1 = 6
            self.cargo_ship2 = 7
            self.cargo_ship3 = 8
            self.roles.append(role.Prospector())
            self.roles.append(role.Prospector())
        else:
            raise ValueError('Invalid number of players')

        # "hand out" starting coins
        self.coins1 = self.coins1 - (num_players * self.start_coins)
        
        # "draw" random face-up plants
        for plant in range(self.face_up_plants):
            rand_plant = self.draw_rand_plant()
            #print 'rand_plant:', rand_plant.name
            self.plants.append(rand_plant)

        # should quarry be appended to list of face-up plants?

        for p in range(num_players):
            new_board = player_board.PlayerBoard(self.start_coins)
            self.player_boards.append(new_board)
            #self.player_boards[p].print_board()

        self.num_players = num_players

    def draw_rand_plant( self ):
        total = self.num_corn + self.num_indigo + self.num_sugar + self.num_tobacco + self.num_coffee
        indigo_div = self.num_corn + self.num_indigo
        sugar_div = indigo_div + self.num_sugar
        tobacco_div = sugar_div + self.num_tobacco
        r = random.randint(1, total)

        if r <= self.num_corn:
            self.num_corn -= 1
            return resource.Corn()
        elif r <= indigo_div:
            self.num_indigo -= 1
            return resource.Indigo()
        elif r <= sugar_div:
            self.num_sugar -= 1
            return resource.Sugar()
        elif r <= tobacco_div:
            self.num_tobacco -= 1
            return resource.Tobacco()
        else:
            self.num_coffee -= 1
            return resource.Coffee()

    def select_role( self ):
        # player takes action and privilege
        # other players take action

        print 'Roles:'
        for i in range(len(self.roles)):
            print i, self.roles[i].name

        sel = int(raw_input('Enter number of selected role: '))
        role = self.roles.pop(sel)
        if role.name == 'Settler':
            # build plants/quarries
            print 'list of plants here'
            pass

    def print_stats( self ):
        print 'Coins (1, 5): {0}, {1}'.format(self.coins1, self.coins5)
        print 'Starting Coins: {0}'.format(self.start_coins)
        print 'Colonists: {0}'.format(self.colonists)
        print 'Colonist Ship: {0}'.format(self.col_ship)
        print 'Cargo Ship 1: {0}'.format(self.cargo_ship1)
        print 'Cargo Ship 2: {0}'.format(self.cargo_ship2)
        print 'Cargo Ship 3: {0}'.format(self.cargo_ship3)
        print 'Points (1, 5): {0}, {1}'.format(self.points1, self.points5)
        print 'Total Points: {0}'.format(self.total_points)
        print 'Face-up plants: {0}'.format(self.face_up_plants)

        print 'Roles:'
        for r in self.roles:
            print r.name
