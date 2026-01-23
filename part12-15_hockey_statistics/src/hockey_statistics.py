# Write your solution here
import json
import re

class Application:
    def __init__(self):
        self.__players = []

    def __help(self):
        commands = '''commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals'''
        print(commands)

    def __read_data(self, file_name):
        with open(file_name) as file:
            data = file.read()
        self.__players = json.loads(data)
        print(f'read the data of {len(self.__players)} players')
    
    def __print_player(self, player):
        return f'{player['name']:21}{player['team']} {player['goals']:3} +{player['assists']:3} = {player['assists']+player['goals']:3}'
    
    def __search_player(self):
        name = input('name: ')
        i = -1
        for ind, player in enumerate(self.__players):
            if player['name'] == name:
                i = ind 
                break
        player = self.__players[i]
        s = self.__print_player(player)
        print(s if i!=-1 else 'Player does not exsist')
    
    def __list_teams(self):
        for team in sorted(set([player['team'] for player in self.__players])):
            print(team)
    
    def __list_nation(self):
        for nation in sorted(set([player['nationality'] for player in self.__players])):
            print (nation)
    
    def __order_by_points(self, player):
        return (player['goals'] + player['assists'], player['goals'])

    def __player_per_team(self):
        team = input('team: ')
        players = [player for player in self.__players if player['team'] == team]
        for player in sorted(players, key=self.__order_by_points, reverse=True):
            print(self.__print_player(player))

    def __player_per_nation(self):
        nation = input('team: ')
        players = [player for player in self.__players if player['nationality'] == nation]
        for player in sorted(players, key=self.__order_by_points, reverse=True):
            print(self.__print_player(player))

    def __most_points(self):
        count = int(input('how many: '))
        players = sorted(self.__players, key=self.__order_by_points, reverse=True)
        for player in players[:count]:
            print(self.__print_player(player))

    def __most_goals(self):
        count = int(input('how many: '))
        players = sorted(self.__players, key=lambda t: (t['goals'],1/t['games']), reverse=True)
        for player in players[:count]:
            print(self.__print_player(player))

    def run(self):
        self.__help()
        self.__read_data(file_name = input('file name: '))
        while True:
            command = int(input('command: '))
            if command == 1:
                self.__search_player()
            elif command == 2:
                self.__list_teams()
            elif command == 3:
                self.__list_nation()
            elif command == 4:
                self.__player_per_team()
            elif command == 5:
                self.__player_per_nation()
            elif command == 6:
                self.__most_points()
            elif command == 7:
                self.__most_goals()
            elif command == 0:
                break
            else:
                self.__help()

app = Application()
app.run()