#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 11:51:41 2023

@author: backmank
"""


# class creation/subclass addition


class Team(object):
    def __init__ (self, team_name):
        self.team_name = team_name
        self.players = []             
    def add_player(self, newplayer):        
        if newplayer not in self.players:
            self.players.append(newplayer)
    def get_players(self):
        return self.players.copy()
    def get_league(self):
         return self.league_name       
    def get_name(self):
        return self.team_name
    def __str__(self):
        if self.players == []:
            return 'Team: '+str(self.team_name)
        else:
            player_str = 'Players:\n'
            for player in self.get_players():
                player_str += str(player.get_player_name()) + ' (' + str(player.get_position()) + ')\n'
            return 'Team: ' + str(self.team_name) + '\n' + player_str
        
class Player(object):
    def __init__(self, player_name, team, position='N/A'):
        self.player_name = player_name
        self.position = position
        self.team = team
        team.add_player(self)
        
    def get_player_name(self):
        return self.player_name
    
    def get_position(self):
        return self.position
    
    def set_position(self,newposition):
        self.position = newposition
    
    def get_player_stat(self):
        return self.player_name + self.get_position() + self.team.get_name()
    

def make_team(player_list, team, position):
    '''
    Parameters
    ----------
    Player_list : List of players youd like to add to a team
        
    team : a string of the name of the team youre looking to fil; with players
        
    position : List of player positions equal length to player_list in order of the players the match the position
        

    Returns 
    -------
    Team filled with players and their positions.
    '''
    if len(player_list) == len(position):
        for i in range(len(player_list)):
            ply = player_list[i]
            pst = position[i]
            Player(ply,team,pst)
        return "mission success!"      
    else:
        return 'mission failed, make matching list lengths'


playas= ['Isagi','Bachira']
positions= ['CF','LM']
bluelock = Team('BlueLock')
make_team(playas, bluelock, positions)
print(bluelock)