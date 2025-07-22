from player import Player
import random

class Bot(Player):
    def __init__(self, money):
        name = random.choice(nome_bot)
        nome_bot.remove(name)
        super().__init__(name, money)


nome_bot = [
    "(BOT) Vitor",
    "(BOT) Megazord",
    "(BOT) Clebin",
    "(BOT) Ultron",
    "(BOT) Jarvis",
    "(BOT) Jessica",
    "(BOT) Julia",
    "(BOT) Jaqueline",
    "(BOT) Jubiscreudis",
    "(BOT) Robisclaudio",
    "(BOT) Robin",
    "(BOT) Roberildo",
    "(BOT) Rolandio",
]