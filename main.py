import random
import os
import sys 
import time

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def roll(self):
        return random.randint(1,6)
    
    def damage(self, damage):
        self.hp -= damage


def get_name():
    return input("What is your name? \n>> ") 

def get_hp():
    return input("How much health would you like to start with? \n>> ")

def dice_roll():
     x = 10
     while x > 0:
        print(random.randint(1,6))
        time.sleep(0.2)
        x-=1
        os.system('clear')

def main ():
    player1_rolls = []
    player2_rolls = []
    os.system('clear')
    player1_name = get_name()
    player2_name = get_name()
    hp = get_hp()
    player1 = Player(player1_name, int(hp))
    player2 = Player(player2_name, int(hp))
    turn = 1
    player1_roll = 0
    player2_roll = 0
    os.system('clear')

    while True:
        if player1.hp > 0 and player2.hp > 0:
            if turn == 1:
                input(f"{player1.name}'s turn. Press enter to attack")
                damage = player1.roll()
                player1_rolls.append(damage)
                os.system('clear')
                dice_roll()
                if damage == player1_roll:
                    print(f"{player1.name} rolled a crit! Roll was: {damage}. Attack is: {damage * 2}")
                    player2.damage(damage * 2)
                else:
                    print(f"{player1.name} rolled a {damage}")
                    player2.damage(damage)
                turn = 2
                player1_roll = damage
                print(f"{player1.name}'s hp = {player1.hp}")
                print(f"{player2.name}'s hp = {player2.hp}")
            elif turn == 2:
                input(f"{player2.name}'s turn. Press enter to attack")
                damage = player2.roll()
                player2_rolls.append(damage)
                os.system('clear')
                dice_roll()
                if damage == player2_roll:
                    print(f"{player2.name} rolled a crit! Roll was: {damage}. Attack is: {damage * 2}")
                    player1.damage(damage * 2)
                else:
                    print(f"{player2.name} rolled a {damage}")
                    player1.damage(damage)
                turn = 1
                player2_roll = damage
                print(f"{player1.name}'s hp = {player1.hp}")
                print(f"{player2.name}'s hp = {player2.hp}")
        elif player1.hp <= 0:
            os.system('clear')
            print(f"{player2.name} is the winner. HP: {player2.hp}")
            print(f"{player1.name}, you lose! HP: ", 0)
            print(f"\n{player1.name}'s rolls: {player1_rolls}")
            print(f"{player2.name}'s rolls: {player2_rolls}")
            sys.exit()
        elif player2.hp <= 0:
            os.system('clear')
            print(f"{player1.name} is the winner. HP: {player1.hp}")
            print(f"{player2.name}, you lose! HP: ", 0)
            print(f"\n{player1.name}'s rolls: {player1_rolls}")
            print(f"{player2.name}'s rolls: {player2_rolls}")
            sys.exit()






main()
