def get_floating_number(p):
    while True:
        try:
            floating_number = float(
                input(f"Enter the {p} floating point number:"))
            return floating_number
        except ValueError:
            print("Please enter a valid floating point number")


def calculation(num1, num2):
    try:
        operator_list = ['+', '-', '*', '/']
        operator = input("Please enter an operator (+,-,*,/):")
        if operator not in operator_list:
            print("Unknown operator")
        elif operator in operator_list:
            if operator == '+':
                print(f"{num1} + {num2} = {num1 + num2}")
            elif operator == '-':
                print(f"{num1} - {num2} = {num1 - num2}")
            elif operator == '*':
                print(f"{num1} * {num2} = {num1 * num2}")
            elif operator == '/':
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2}")
                elif num2 == 0:
                    print("Cannot divide by zero")
    except ZeroDivisionError:
        pass


def main():
    first_number = get_floating_number("first")
    second_number = get_floating_number("second")
    calculation(first_number, second_number)


if __name__ == "__main__":
    main()
