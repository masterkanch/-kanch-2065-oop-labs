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

    def display_factors(number):
        number = int(number)
        if number % 2 == 0:
            return f'Factors of {number} is {number/2} and {number/2}'
        else:
            return f'Factors of {number} is {math.floor(number/2)} and {round(number/2)}'

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
