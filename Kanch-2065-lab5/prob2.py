"""
Kanch Ruansiripiyakul 633040206-5

Program that caluculate hypotenuse
"""
import math


def hypotenuse(num1, num2):
    try:
        result = math.sqrt(math.pow(num1, 2) + math.pow(num2, 2))
        return result
    except TypeError:
        num1 = float(num1)
        num2 = float(num2)
        result = math.sqrt(math.pow(num1, 2) + math.pow(num2, 2))
        return result


if __name__ == "__main__":
    print(f"hypotenuse(3,4) is {hypotenuse(3.0,4.0)}")
    print(f"hypotenuse('3','4') is {hypotenuse('3','4')}")
    print(f"hypotenuse(3,'4.0') is {hypotenuse(3.0,'4.0')}")
