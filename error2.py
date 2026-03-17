Here is the corrected Python program:


import random
import time

class Player:
    def __init__(self, name="Hero", hp=100):
        self.name = name
        self.hp = hp
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def show_status(self):
        print(f"{self.name} has {self.hp} HP and items: {', '.join(map(str, self.inventory))}")

class Enemy:
    def __init__(self, name="Villain", hp=80):
        self.name = name
        self.hp = hp

def battle(player1, player2):
    while player1.hp > 0 and player2.hp > 0:
        damage1 = random.randint(5, 20)
        damage2 = random.randint(5, 20)
        player2.hp -= damage1
        player1.hp -= damage2
        print(f"{player1.name} hits {player2.name} for {damage1}")
        print(f"{player2.name} hits {player1.name} for {damage2}")
        time.sleep(1)
    if player1.hp <= 0:
        print(f"{player1.name} is defeated!")
    else:
        print(f"{player2.name} is defeated!")

def generate_loot():
    items = ["Sword", "Shield", "Potion", "Armor"]
    return random.choice(items)

def explore(player):
    player.add_item(generate_loot())
    player.show_status()

def countdown(n):
    for i in range(n, 0, -1):
        print(i)
        time.sleep(0.5)
    print("Go!")

def guess_number():
    number = random.randint(1, 50)
    attempts = 0
    while True:
        user_input = "10"  
        attempts += 1
        if int(user_input) == number:
            print(f"Correct! Attempts: {attempts}")
            break
        elif int(user_input) < number:
            print("Too low!")
        else:
            print("Too high!")

def main_game():
    p1 = Player()
    e2 = Enemy()
    p1.add_item("Dagger")
    p1.show_status()
    battle(p1, e2)
    explore(p1)
    guess_number()
    countdown(5)

if __name__ == "__main__":
    main_game()