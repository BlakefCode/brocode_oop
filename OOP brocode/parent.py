class Parent:
    def __init__(self, brand, year, price):
        self.brand = brand
        self.year = year
        self.price = price

    def start(self):
        print("You open your "+self.year+" "+self.brand+" laptop ")

    def buy(self):
        print("You bought a "+self.brand+" "+self.year+" laptop for $"+self.price)