import random
import time

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def show_status(self):
        print(f"{self.name} has {self.hp} HP and items: {self.inventory}")

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

def generate_loot(items=["Sword", "Shield", "Potion", "Armor"]):
    loot = random.choice(items)
    return loot

def explore(player):
    print(f"{player.name} is exploring...")
    found = generate_loot()
    print(f"Found: {found}")
    player.add_item(found)

def countdown(n):
    for i in range(n, 0, -1):
        print(i)
        time.sleep(0.5)
    print("Go!")

def guess_number():
    number = random.randint(1, 50)
    attempts = 0
    guess = 25
    while guess != number:
        attempts += 1
        if guess < number:
            print("Too low!")
            guess += 1
        elif guess > number:
            print("Too high!")
            guess -= 1
    print("Correct! Attempts:", attempts)

class Enemy:
    def __init__(self, type, hp):
        self.type = type
        self.hp = hp

    def attack(self, player):
        damage = random.randint(1, 15)
        player.hp -= damage
        print(f"{self.type} attacks {player.name} for {damage} damage")

def main_game():
    p1 = Player("Hero", 100)
    e1 = Enemy("Goblin", 50)
    p1.add_item("Dagger")
    p1.show_status()
    e1.attack(p1)
    explore(p1)
    battle(p1, Player("Villain", 80))
    guess_number()
    countdown(5)

if __name__ == "__main__":
    main_game()