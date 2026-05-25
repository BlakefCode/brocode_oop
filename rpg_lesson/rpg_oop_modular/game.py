from models import Character, Boss, Weapon
from utils import clear_screen, press_enter, print_border

class Game:
    def __init__(self):
        self.player = None
        self.bosses = []

    def show_intro(self):
        clear_screen()
        print("Welcome to the RPG Adventure!")
        print("\nIn a world where darkness looms, you are the chosen hero destined to defeat the evil bosses and restore peace.")
        self.setup_game(input("\nEnter your character's name: ").capitalize())

    def setup_game(self, name):
        self.player = Character(name, 110, 10, self.choose_weapon())
        self.player.display()
        press_enter()
        self.bosses = [Boss("Goblin King", 50, 8), Boss("Dark Sorcerer", 60, 9)]

    def choose_weapon(self):
        weapons = [
            {"name": "Rock", "damage_bonus": 2},
            {"name": "Paper", "damage_bonus": 3},
            {"name": "Scissors", "damage_bonus": 4}
        ]
        options = [weapon["name"] for weapon in weapons]
        choice_index = self.get_input("\nChoose your weapon (Rock, Paper, Scissors): ", options)
        weapon_data = weapons[choice_index]
        return Weapon(weapon_data["name"], weapon_data["damage_bonus"])

    def get_input(self, prompt, options):
        while True:
            user_input = input(prompt).capitalize()
            if user_input in options:
                return options.index(user_input)
            print("Invalid input, please try again.")

    def combat(self, player, enemy):
        while player.health > 0 and enemy.health > 0:
            self.display_combat_status(player, enemy)
            damage_dealt = player.attack(enemy)
            print(f"You dealt {damage_dealt} damage to {enemy.name}.")
            if enemy.health <= 0:
                self.print_victory_message(enemy)
                return True

            damage_received = enemy.attack(player)
            print(f"{enemy.name} dealt {damage_received} damage to you.")
            if player.health <= 0:
                self.print_defeat_message(enemy)
                return False

            press_enter()

    def display_combat_status(self, player, enemy):
        clear_screen()
        level = "LEVEL 1" if enemy.name == "Goblin King" else "LEVEL 2"
        print(f"\n==============> {level}: {enemy.name} <=============")
        player.display()
        enemy.display()
        press_enter()

    def handle_boss_battles(self):
        for boss in self.bosses:
            self.introduce_boss(boss)
            if not self.combat(self.player, boss):
                self.end_game(False)
                return
        self.end_game(True)

    def introduce_boss(self, boss):
        clear_screen()
        intro_messages = {
            "Goblin King": f"Level 1 - You have entered the lair of the Goblin King. He is known for his strength and brutality. Prepare for battle, {self.player.name}!",
            "Dark Sorcerer": f"Level 2 - You have defeated the Goblin King! Now, you face the Dark Sorcerer, a master of dark magic. Good luck, {self.player.name}!"
        }
        print(intro_messages.get(boss.name, "A new boss appears!"))
        press_enter()

    def print_victory_message(self, enemy):
        print_border()
        print(f"Victory! You defeated {enemy.name}.")
        press_enter()

    def print_defeat_message(self, enemy):
        print_border()
        print(f"Defeat! You were defeated by {enemy.name}.")
        press_enter()

    def end_game(self, player_won):
        print_border()
        if player_won:
            print(f"Congratulations, {self.player.name}! You defeated all the bosses and restored peace to the land!")
        else:
            print(f"Game Over. The darkness prevails, but heroes never give up. Try again, {self.player.name}!")
        print_border()

    def run(self):
        self.show_intro()
        self.handle_boss_battles()