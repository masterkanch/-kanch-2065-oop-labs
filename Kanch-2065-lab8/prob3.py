"""
Kanch Ruansiripiyakul 633040206-5
"""


class Pet:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"I'm {self.name}")

    def move(self):
        print(f"moving...")


class Cat(Pet):
    def __init__(self, name, owner, color):
        super().__init__(name)
        self.owner = owner
        self.color = color

    def move(self):
        print("Cat likes to walk more than run")

    def show_info(self):
        super().show_info()
        print(f" and is {self.color}")
        print(f" belonging to {self.owner}")


class Dog(Pet):
    def __init__(self, name, owner, color):
        super().__init__(name)
        self.owner = owner
        self.color = color

    def move(self):
        print("Dog likes to run more than walk")

    def show_info(self):
        super().show_info()
        print(f" and is {self.color}")
        print(f" belonging to {self.owner}")

    def eat_cat(self, para):
        print(f"Dog {self.name} eats cat {para.name}")


if __name__ == "__main__":
    pet1 = Pet("Thongdaeng")
    pet1.show_info()
    pet1.move()
    cat1 = Cat("Thongdee", "Manee", "white")
    cat1.show_info()
    cat1.move()
    dog1 = Dog("Thongdum", "Manee", "black")
    dog1.show_info()
    dog1.move()
    dog1.eat_cat(cat1)
