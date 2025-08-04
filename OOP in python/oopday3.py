#composition in oop
class Engine:
    def start(self) -> str:
        return"engine started"
class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self) -> str:
        return self.engine.start() + " | car is moving"
my_car = Car()
print(my_car.drive())


class Ride:
    def __init__(self):
        self.engine = Engine()
    def drive_ride(self) -> str:
        return self.engine.start() + "|and riding it."
rodeo = Ride()
print(rodeo.drive_ride())
