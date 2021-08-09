def get_floating_number(p):
    while True:
        try:
            floating_number = float(
                input(f"Enter the {p} floating point number:"))
            return floating_number
        except ValueError:
            print("Please enter a valid floating point number")


def get_operator():
    operator_list = ['+', '-', '*', '/']
    while True:
        try:
            operator = input("Please enter an operator (+,-,*,/):")
            if operator not in operator_list:
                print("Please enter a valid operator")
                continue
            elif operator in operator_list:
                return operator
        except ValueError:
            print("Please enter a valid operator")


def calculation(num1, num2, operator):
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
    except ZeroDivisionError:
        pass


def main():
    first_number = get_floating_number("first")
    second_number = get_floating_number("second")
    operator = get_operator()
    calculation_num = calculation(first_number, second_number, operator)
    if operator == '/' and second_number == 0.0:
        print("Cannot division by zero")
    else:
        print(f"{first_number} {operator} {second_number} = {calculation_num}")


if __name__ == "__main__":
    main()
