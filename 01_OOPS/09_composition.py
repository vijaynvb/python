 
class Engine:
    def start(self):
        print("Engine Started")


 
class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        print("Starting Car...")
        self.engine.start()


 
car = Car()
car.start_car()