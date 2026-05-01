class Parent:
    def __init__(self, name, age, catchphrase):
        self.name = name
        self.age = age
        self.catchphrase = catchphrase
    
    def activity(self):
        return "working and taking care of the family"
    
    def speak(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old. {self.catchphrase} I enjoy {self.activity()}.")


class Child(Parent):
    def __init__(self, name, age, catchphrase):
        super().__init__(name, age, catchphrase)
        self.activities = {
            "Bart": "skateboarding and pulling pranks",
            "Lisa": "playing saxophone and reading books",
            "Maggie": "playing with her pacifier and exploring"
        }
    
    def activity(self):
        return self.activities.get(self.name, "playing and having fun")
    
    def speak(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old. {self.catchphrase} I love {self.activity()}!")




