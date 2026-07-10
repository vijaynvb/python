class Car:
    def start(self):
        print("Car starts with a key or push button")

class Bike:
    def start(self):
        print("Bike starts with a self-start button")

class Truck:
    def start(self):
        print("Truck starts with a heavy-duty ignition system")


vehicles = [Car(), Bike(), Truck()]

for vehicle in vehicles:
    vehicle.start()