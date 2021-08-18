"""
Kanch Ruansiripiyakul 633040206-5

Program that caluculate factorial with recursion algorithm.
"""


def get_number():
    while True:
        try:
            integer = int(input("Enter a non-negative integer:"))
            if integer < 0:
                print("Please enter an integer that is non-negative")
                break
            else:
                return integer  # print value

        except ValueError:
            print("Please enter a valid integer")
            break


def recursive_factorial(integer):
    try:
        if integer == 1:
            return 1
        else:
            return integer * recursive_factorial(integer - 1)
    except TypeError:
        pass


if __name__ == '__main__':
    number = get_number()
    factorial_of_number = recursive_factorial(number)
    if number is not None:
        print(f"The factorial of {number} is {factorial_of_number}")
