"""
Kanch Ruansiripiyakul 633040206-5
"""

"""
prob1.py:This file illustrates the usage of an abstract class
"""




import abc
class Animal(abc.ABC):
    """Class Animal is an abstarct class that has abstract method move"""
    @abc.abstractmethod
    def move(self):
        """Method move is an abstract method of an abstract class Animal"""
        pass


class Human(Animal):
    def move(self):
        print("I can walk and run")


class Snake(Animal):
    def move(self):
        print("I can crawl")


class Dog(Animal):
    def move(self):
        print("I can bark")


if __name__ == "__main__":
    print(__doc__)
    print(Animal.__doc__)
    print(Animal.move.__doc__)
    print("=== Below is the output of the code ===")
    human = Human()
    human.move()
    snake = Snake()
    snake.move()
    dog = Dog()
    dog.move()
