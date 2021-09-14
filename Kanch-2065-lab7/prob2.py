"""
Kanch Ruansiripiyakul 633040206-5
"""
import math


class Numbers:
    def __init__(self, first_number, second_number):
        self.first_number = int(first_number)
        self.second_number = int(second_number)

    def add(self):
        return self.first_number + self.second_number

    @classmethod
    def display_factors(cls, number):
        number = int(number)
        second_number = cls.second_number = number / 2
        if number % 2 == 0:
            return f'Factors of {number} is {second_number} and {second_number}'
        else:
            return f'Factors of {number} is {math.floor(second_number)} and {round(second_number)}'

    @staticmethod
    def is_valid_divisor(number):
        if number == 0:
            return '0 is not a valid divisor'
        else:
            return f'{number} is a valid divisor'


if __name__ == "__main__":
    print(f'2 + 3 is {Numbers(2,3).add()}')
    print(Numbers.display_factors(6))
    print(Numbers.display_factors(7))
    print(Numbers.is_valid_divisor(2))
    print(Numbers.is_valid_divisor(0))
