def get_floating_number(p):
    while True:
        try:
            floating_number = input(f"Enter the {p} operand ('q' to quit):")
            if floating_number == 'q' or floating_number == 'Q':
                break
            return float(floating_number)
        except ValueError:
            print("Invalid floating point")


def get_operator():
    operator_list = ['+', '-', '*', '/']
    try:
        operator = input("Enter an operation (+,-,*,/):")
        if operator in operator_list:
            return operator
        elif operator not in operator_list and operator:
            print("Operation must be ADD, SUB , MUL or DIV.")
            return 'continue loop'
        elif not operator:
            return '+'

    except ValueError:
        print("Operation must be ADD, SUB , MUL or DIV.")


def get_format():
    output_format_list = ['float', 'int']
    try:
        output_format = input("Enter output format (float, int):")
        if output_format in output_format_list:
            return output_format
        elif not output_format:
            return 'float'
        elif output_format not in output_format_list and output_format:
            print("Enter a valid output format (float, int)")
            return 'continue loop'
    except ValueError:
        print("Enter a valid output format (float, int)")


def robust_calculator(num1, num2, operator, format):
    try:
        if format == "float":
            num1 = float(num1)
            num2 = float(num2)
            if operator == '+':
                print(f"{num1} + {num2} = {num1 + num2:0.02f}")
            elif operator == '-':
                print(f"{num1} - {num2} = {num1 - num2:0.02f}")
            elif operator == '*':
                print(f"{num1} * {num2} = {num1 * num2:0.02f}")
            elif operator == '/':
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 // num2:0.02f}")
                elif num2 == 0:
                    print("Cannot divide by zero")
        elif format == "int":
            if operator == '+':
                print(f"{num1} + {num2} = {int(num1 + num2)}")
            elif operator == '-':
                print(f"{num1} - {num2} = {int(num1 - num2)}")
            elif operator == '*':
                print(f"{num1} * {num2} = {int(num1 * num2)}")
            elif operator == '/':
                if num2 != 0:
                    print(f"{num1} / {num2} = {int(num1 // num2)}")
                elif num2 == 0:
                    print("Cannot divide by zero")
                    print("We cannot perform your requested calculation")
    except ZeroDivisionError:
        pass


def main():
    while True:
        num1 = get_floating_number('first')
        if num1 == None:
            break
        num2 = get_floating_number('second')
        if num2 == None:
            break
        operator = get_operator()
        if operator == 'continue loop':
            continue
        output_format = get_format()
        if output_format == 'continue loop':
            continue
        robust_calculator(num1, num2, operator, output_format)


if __name__ == "__main__":
    main()
