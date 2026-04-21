#Parent class that all child classes will inherit from
class Vehicle:
    def __init__(self, make, model):        
        self.make = make
        self.model = model

    def __str__(self):
        return f"This is a {self.make}, {self.model}"
    
    def move(self):
        print("Move from here to there")

#Child class that will inherit from Vehicle
class Boat(Vehicle):
    #LONG WAY (DO NOT USE)
    # def __init__ (self, make, model, towbar, stereo):
    #     self.make = make
    #     self.model = model
    #     self.towbar = towbar
    #     self.stereo = stereo
    #BETTER
    def __init__ (self, make, model, towbar, stereo):
        #calls the constructor from the parent class so we do not have to define what to do with make, model
        super().__init__(make, model) 
        self.towbar = towbar
        self.stereo = stereo 

    def __str__(self):
        # has_stereo = "has"
        # if self.stereo ==False:
        #     has_stero = "does not have"
        return f"This is a {self.make}, {self.model} and {"has" if self.stereo else "does not have"} a stereo"
    def move(self):
        print("Floats from here to there")

    #Create the Car and Airplane classes
class Car(Vehicle):
    def __init__ (self, make, model, horsepower, sunroof):        
        super().__init__(make, model) 
        self.horsepower = horsepower
        self.sunroof = sunroof
    def move(self):
        print("Drives from here to there")

class Airplane(Vehicle):
    def __init__ (self, make, model, flaps):        
        super().__init__(make, model) 
        self.flaps = flaps
    def move(self):
        print("Flies from here to there")

my_boat = Boat("SS","Mino",False, True)
print(my_boat)
my_boat.move()

my_car = Car("Ford","F150",250,True)
print(my_car)
my_car.move()

my_plane = Airplane("Cesna","B12",True)
print(my_plane)
my_plane.move()

#Polymorphism is methods that have the same name but different results/behaviors
#move() has 4 different results here

print("\n\nPolymorphism")
for vehicle in (my_boat,my_car,my_plane):
    vehicle.move()

        





        