#Date: 23/02/2026
#program to show classes in python

class Car():
    #attributes of the car
    def __init__(self,model,make,colour,year):
        self.model = model
        self.make = make
        self.colour = colour
        self.year = year
    #print car details
    def print_details (make,model,colour,year):
        print(f"{make}{model} is a {colour} car made in {year}")
        #initializethe class details
        my_car=Car("audi","q8","black",2025)
        my_dad_car=Car("mercedes","benz","white",2024)

        my_car.print_details(self.model,self.make,self.colour,self.year)
        my_dad_car.print_details("self.model,self.make,self.colour,self.year)
        print(f"the car is a {self.make} {self.model} of colour {self.colour} and was made in {self.year}")
