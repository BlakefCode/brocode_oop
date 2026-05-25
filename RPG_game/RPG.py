import time
from main import Character

# Create parent characters
player_name = input("Player enter your name: ")
player_inventory = [ ]
player_race = ' '
player_item = ' '
player_strength = 0
player_speed = 0
player_intelligence = 0

chosen_race = int(input("\n1.Elf\n2.Dwarf\n3.Orc\n4.Wizard\n5.Mage\nWhat race do you want to be?: "))

def race():
    global player_race, player_item, player_strength, player_speed, player_intelligence
    if chosen_race == 1:
        player_race = 'Elf'
        print(player_name,"You have chosen the Elf race.")
    elif chosen_race == 2:
        player_race = 'Dwarf'
        print(player_name,"You have chosen the Dwarf race.")
    elif chosen_race == 3:
        player_race = "Orc"
        print(player_name, "You have chosen the Orc race.")
    elif chosen_race == 4:
        player_race = "Wizard"
        print(player_name, "You have chose the Wizard race.")
    elif chosen_race == 5:
        player_race = "Mage"
        print(player_name, "You have chose the Mage race.")
    else:
        print("Invalid choice. Please try again.")

race()
time.sleep(1)
player_character = Character(player_race, player_name, player_strength, player_speed, player_intelligence, player_item, player_inventory)
print("\n")

text = """Long ago, the magical crystal protecting Elaris shattered, covering the kingdom in darkness.
Monsters roam the land, and ancient ruins have awakened.
You are a traveler chosen by the crystal’s power, tasked with finding its lost fragments before the world falls forever."""

for c in text:
    print(c, end="")
    time.sleep(0.02)