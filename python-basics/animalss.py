#name:triza mwaura
#date:23/02/2026
#program to show inheritance in Python

class Animal:
    def __init__(self, species, weight, food):
        self.species = species
        self.weight = weight
        self.food = food

    def grow(self, weight):
        weight = 1.1 * weight
        print(f"The animal weighs {weight}kg")

    def eat(self, food):
        print(f"The animal eats {food}")


class Dog(Animal):
    def __init__(self, species, weight, food, color, height, breed):
        super().__init__(species, weight, food)
        self.color = color
        self.height = height
        self.breed = breed

    def bark(self):
        print("The dog says woof woof")


class Horse(Animal):
    def __init__(self, species, weight, food):
        super().__init__(species, weight, food)

    def neigh(self):
        print("The horse says neigh neigh")
                


