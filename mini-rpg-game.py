import random

player_hp = 20
monster_hp = 15

while player_hp > 0 and monster_hp > 0:
    input("Press Enter to attack!")

    damage = random.randint(1, 6)
    monster_hp -= damage
    print(f"You hit for {damage} damage!")

    if monster_hp <= 0:
        print("🏆 Monster defeated!")
        break

    damage = random.randint(1, 4)
    player_hp -= damage
    print(f"Monster hits for {damage} damage!")

    print(f"❤️ HP: {player_hp}")
    print(f"👹 Monster HP: {monster_hp}\n")

if player_hp <= 0:
    print("💀 Game Over")
