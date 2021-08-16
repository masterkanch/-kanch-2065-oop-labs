"""
Kanch Ruansiripiyakul 633040206-5

Program that caluculate hypotenuse
"""
import math


def hypotenuse(num1, num2):
    result = math.sqrt(math.pow(num1, 2) + math.pow(num2, 2))
    print(f"Sqrt({num1}^2 + {num2}^2) = {result}")


def main():
    hypotenuse(3.0, 4.0)
    hypotenuse(3, 4)
    hypotenuse(3, 4.0)


if __name__ == "__main__":
    main()
