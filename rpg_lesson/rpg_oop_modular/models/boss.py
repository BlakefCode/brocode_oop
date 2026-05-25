from .character import Character
from .weapon import Weapon

class Boss(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Weapon("Boss Weapon", 5))

    def attack(self, enemy):
        additional_damage = 1
        total_damage = super().attack(enemy)
        enemy.health -= additional_damage
        print(f"{self.name} uses a special attack! (+{additional_damage} Damage)")
        return total_damage + additional_damage