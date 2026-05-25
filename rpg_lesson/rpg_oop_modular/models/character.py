from .weapon import Weapon

class Character:
    def __init__(self, name, health, damage, Weapon=None):
        self.name = name
        self.health = health
        self.damage = damage
        self.weapon = Weapon

    def attack(self, enemy):
        total_damage = self.damage + (self.weapon.damage_bonus if self.weapon else 0)
        enemy.health -= total_damage
        return total_damage

    def display(self):
        weapon_name = self.weapon.name if self.weapon else 'No Weapon'
        weapon_damage = self.weapon.damage_bonus if self.weapon else 0
        print(f"\nName: {self.name}\nHealth: {self.health}\nDamage: {self.damage}\nWeapon: {weapon_name} (+{weapon_damage} Damage)")