import random

player = {
    "name": "",
    "class": "",
    "hp": 100,
    "gold": 10,
    "inventory": ["Wooden Sword"]
}

monsters = [
    ("Goblin", 20),
    ("Skeleton", 30),
    ("Wolf", 25),
    ("Orc", 40)
]

def stats():
    print("\n====== PLAYER ======")
    print("Name:", player["name"])
    print("Class:", player["class"])
    print("HP:", player["hp"])
    print("Gold:", player["gold"])
    print("Inventory:", ", ".join(player["inventory"]))

def explore():
    monster = random.choice(monsters)
    print(f"\nA wild {monster[0]} appears!")

    while monster[1] > 0 and player["hp"] > 0:
        print("\n1. Attack")
        print("2. Run")

        choice = input("> ")

        if choice == "1":
            damage = random.randint(8,20)
            monster_hp = monster[1] - damage

            print(f"You hit the {monster[0]} for {damage} damage!")

            if monster_hp <= 0:
                print(f"You defeated the {monster[0]}!")
                reward = random.randint(5,15)
                player["gold"] += reward
                print(f"You found {reward} gold!")
                break

            enemy = random.randint(4,12)
            player["hp"] -= enemy
            print(f"The {monster[0]} hits you for {enemy} damage.")

            monster = (monster[0], monster_hp)

        elif choice == "2":
            print("You escaped!")
            break

def heal():
    if player["gold"] >= 5:
        player["gold"] -= 5
        player["hp"] += 20
        if player["hp"] > 100:
            player["hp"] = 100
        print("You healed 20 HP.")
    else:
        print("Not enough gold.")

print("==== RETRO MATT RPG ====")

player["name"] = input("Enter your name: ")

print("\nChoose a class")
print("1. Warrior")
print("2. Mage")
print("3. Rogue")

choice = input("> ")

classes = {
    "1":"Warrior",
    "2":"Mage",
    "3":"Rogue"
}

player["class"] = classes.get(choice,"Adventurer")

while player["hp"] > 0:

    print("\n====== MENU ======")
    print("1. Explore")
    print("2. Heal")
    print("3. Stats")
    print("4. Quit")

    option = input("> ")

    if option == "1":
        explore()

    elif option == "2":
        heal()

    elif option == "3":
        stats()

    elif option == "4":
        break

print("\nGame Over!")
