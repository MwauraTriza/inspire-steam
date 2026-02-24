#name:triza mwaura
#date:19/02/2026
#program to show inheritance in python

class Animal: 
    def __init__(self, colour, weight, barks, breed):
        super.colour=colour
        self.weight=weight
        self.barks=barks
        self.breed=breed
    
    def grow(self,weight):
        weight=1.1*weight
        print(f"The animal weight is now {weight}kg")

    def barks(self):
        print("the dog says woof")

        

class Animal(horse):
    def __init__(self, species, weight, neighs):
        self.species=species
        self.weight=weight
        self.food=food
    
    def grow(self,weight):
        weight=1.1*weight
        print(f"The animal weight is now {weight}kg")

    def