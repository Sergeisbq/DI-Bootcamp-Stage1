class Car:

    def __init__(self, speed) -> None:
        self.speed = speed

    # > - greater than
    def __gt__(self, other_car):
        return self.speed > other_car.speed

    # > - less than
    def __lt__(self, other_car):
        return self.speed < other_car.speed

    # == - equal
    def __eq__(self, other_car):
        return self.speed == other_car.speed
    
    # + - plus
    def __iadd__(self, other_car):
        self.speed += other_car.speed
        return self

car1 = Car(200)
car2 = Car(300)

car1 += car2
print(car1.speed)