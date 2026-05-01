from homer_class import Parent, Child

# Create parent characters
homer = Parent("Homer", 39, "D'oh!")
marge = Parent("Marge", 36, "Mmmmm...")

# Create child characters
bart = Child("Bart", 10, "Eat my shorts!")
lisa = Child("Lisa", 8, "It's a perfect day!")
maggie = Child("Maggie", 1, "*suck* *suck*")

homer.speak()
marge.speak()
bart.speak()
lisa.speak()
maggie.speak()
