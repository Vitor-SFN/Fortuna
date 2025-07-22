class Table:
    pot = 0
    players = []

    #def __init__(NONE):
    #    NONE

    def add_players(self, *players):
        for player in players:
            Table.players.append(player)