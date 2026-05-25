class Character:
    def __init__(self, name, race, strength, speed, intelligence, item, inventory):
        self.race = race
        self.strength = strength
        self.speed = speed
        self.intelligence = intelligence
        self.item = item
        self.inventory = inventory
        self.name = name

    def pickup(self):
        print(f"{self.race} picked up {self.item}")

    def move(self):
        print(f"{self.name} moved to the next room")

