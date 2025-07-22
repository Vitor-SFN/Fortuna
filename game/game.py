from player import Player


class Game:
    time_max_per_round = 60
    number_of_players = 0
    start_money = 1000
    debug_mode = True
    players = []

    @staticmethod
    def main_menu():
        while True:
            print("#----Welcome to the game----------#")
            print("1 - Start game")
            print("2 - Add new player")
            print("3 - Game Settings")
            print("4 - Quit")
            print("#---------------------------------#")
            option = input()
            Game.actions_main_menu.get(option, lambda: print("Invalid command, try again!"),)()


    @staticmethod
    def show_settings():
        print("#--------------Game settings--------------#")
        print(f"1 - Time per each round: {Game.time_max_per_round} seconds")
        print(f"2 - Start Money: {Game.start_money} (Does not apply to the players that you manually put the values on)")
        if not Game.players:
            print("There are no players, please add them!")
        else:
            print(f"3 - Players: {', '.join(player.name for player in Game.players)}")
        print("#-----------------------------------------#")
        print("If you want to change anything, just type the respective number of the option. (To get back, just type anything else)")
        option = input()
        Game.actions_setting_menu.get(option, lambda: print(""))()


    @staticmethod
    def start_game():
        for player in Game.players:
            if not player.money_altered:
                player.money = Game.start_money
        print("Starting game...")

    @staticmethod
    def settings():
        Game.show_settings()

    @staticmethod
    def quit():
        print("Thank you for playing...")

    @staticmethod
    def add_new_player():
        print("What's the name of the player?")
        name = input()
        player = Player(name, Game.start_money)
        Game.players.append(player)
        Game.number_of_players += 1

    @staticmethod
    def set_time_max_per_round():
        print("How many seconds do you want to set the time per each round?")
        Game.time_max_per_round = int(input())

    @staticmethod
    def set_start_money():
        print("What's the starting money?")
        Game.start_money = int(input())

    @staticmethod
    def change_player_status():
        if not Game.players:
            return
        count = 1
        for player in Game.players:
            print(f"+-----------Player {count}---------------------+")
            print(f"| {player.name}'s money: {player.money}")
            print("+----------------------------------------+")
            count += 1
        print("put the number of the player you want to change")
        player = int(input())
        print("What do you want to change?")
        print("1 - Name")
        print("2 - Start money")
        option = input()
        if option == "1":
            print("Set the new name:")
            name = input()
            Game.players[player-1].name = name
        elif option == "2":
            print("Set the new money:")
            start_money = int(input())
            Game.players[player-1].money = start_money
            Game.players[player-1].money_altered = True
        else:
            print("Invalid option")


    actions_main_menu = {
        '1': start_game,
        '2': add_new_player,
        '3': settings,
        '4': quit
    }

    actions_setting_menu = {
        '1': set_time_max_per_round,
        '2': set_start_money,
        '3': change_player_status
    }