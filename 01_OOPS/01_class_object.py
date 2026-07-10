class Vehicle:
    def __init__(self, identity, color):
        self.identity = identity
        self.color = color

    def drive(self):
        print(f"{self.identity} is driving")

    def brake(self):
        print(f"{self.identity} is braking")

    def accelerate(self):
        print(f"{self.identity} is accelerating")


 
bike = Vehicle("Bike", "Red")

print("Identity:", bike.identity)
print("Color:", bike.color)

bike.drive()
bike.brake()
bike.accelerate()