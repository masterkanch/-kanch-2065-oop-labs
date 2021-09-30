"""
Kanch Ruansiripiyakul 633040206-5
"""


class Vehicle:
    def __init__(self, name, speed, mileage):
        self.name = name
        self.__speed = speed
        self.mileage = mileage

    def __str__(self):
        return f"Name:{self.name} speed: {self.__speed} mileage: {self.mileage}"

    def set_speed(self, speed):
        self.__speed = speed


class Car(Vehicle):
    def __init__(self, name, speed, mileage, num_doors):
        super().__init__(name, speed, mileage)
        self.num_doors = num_doors

    def __str__(self):
        return f"{super().__str__()} num doors: {self.num_doors}"


class Bus(Vehicle):
    def __init__(self, name, speed, mileage, capacity):
        super().__init__(name, speed, mileage)
        self.capacity = capacity

    def __str__(self):
        return f"{super().__str__()} capacity: {self.capacity}"


if __name__ == "__main__":
    car = Car("Toyota Vios", 90, 150000, 4)
    bus = Bus("School Volvo", 12, 20000, 100)
    print(car)
    print(bus)
    bus.set_speed(30)
    print(bus)
