#!/usr/bin/env python

import role
import main_board
import player_board

class Game( object ):
    
    def __init__( self, num_players ):
        self.coins1 = 46
        self.coins5 = 8
        self.points1 = 32
        self.points5 = 18

        self.roles = set([role.Settler(), role.Mayor(), role.Builder(), role.Craftsman(),
                role.Trader(), role.Captain()])

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
            self.roles.add(role.Prospector())
        elif num_players == 5:
            self.start_coins = 4
            self.total_points = 122
            self.colonists = 95
            self.cargo_ship1 = 6
            self.cargo_ship2 = 7
            self.cargo_ship3 = 8
            self.roles.add(role.Prospector())
            self.roles.add(role.Prospector())
        else:
            raise ValueError('Invalid number of players')

        self.face_up_plants = num_players + 1
        self.col_ship = num_players

        self.coins1 = self.coins1 - (num_players * self.start_coins)

        self.board = main_board.Board(num_players)
        self.player_boards = []

        for p in range(num_players):
            new_board = player_board.PlayerBoard(self.start_coins)
            self.player_boards.append(new_board)
            self.player_boards[p].print_board()
        
        self.num_players = num_players

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
