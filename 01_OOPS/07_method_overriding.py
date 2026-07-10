class Vehicle:

    def get_mileage(self):
        print("Mileage information not available")

    def get_cost(self):
        print("Cost information not available")


 
class Car(Vehicle):

    def get_mileage(self):
        print("Car Mileage: 18 km/l")

    def get_cost(self):
        print("Car Cost: ₹10,00,000")


 
class Bike(Vehicle):

    def get_mileage(self):
        print("Bike Mileage: 55 km/l")

    def get_cost(self):
        print("Bike Cost: ₹1,20,000")


 
car = Car()
bike = Bike()

print("Car Details:")
car.get_mileage()
car.get_cost()

print("\nBike Details:")
bike.get_mileage()
bike.get_cost()