from player import Player

class Game:
    time_max_per_round = 60
    number_of_players = 0
    start_money = 1000
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
            Game.actions.get(option, lambda: print("Invalid command, try again!"),)()


    @staticmethod
    def show_settings():
        print("Game settings: ")
        print(f"Time per each round: {Game.time_max_per_round} seconds")
        print(f"Start Money: {Game.start_money}")
        if not Game.players:
            print("There are no players, please add them!")
        else:
            print(f"Players: {', '.join(player.name for player in Game.players)}")

    @staticmethod
    def start_game():
        for player in Game.players:
            player.money -= Game.start_money
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

    actions = {
        '1': start_game,
        '2': add_new_player,
        '3': settings,
        '4': quit
    }