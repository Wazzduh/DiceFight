import random

class Player:
    def __init__(self, name, hp):
        self.name = name
        seslf.hp = hp


def get_name():
    return input("What is your name? \n>>") 

def roll():
    return random.randint(1,6)

def main ():

    player1 = Player(get_name(), 100)
    player2 = Player(get_name(), 100)

    print(player1.name)
    print(player2.name)




main()
