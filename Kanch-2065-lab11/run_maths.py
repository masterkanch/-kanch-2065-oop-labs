import sys
"""
Kanch Ruansiripiyakul 633040206-5
"""

operator_list = ['+', '-', 'x', '/']
if __name__ == '__main__':
    try:
        num_args = len(sys.argv) - 1
        operator = sys.argv[1]
        operand1 = float(sys.argv[2])
        operand2 = float(sys.argv[3])

        if operator in operator_list:
            if operator == '+':
                print(f"{operand1} + {operand2} is {operand1 + operand2}")
            elif operator == '-':
                print(f"{operand1} - {operand2} is {operand1 - operand2}")
            elif operator == 'x':
                print(f"{operand1} x {operand2} is {operand1 * operand2}")
            elif operator == '/':
                if operand2 != 0:
                    print(f"{operand1} / {operand2} = {operand1 / operand2}")
                elif operand2 == 0:
                    try:
                        print(f"{operand1} cannot divide by zero")
                    except ZeroDivisionError:
                        print(f"{operand1} cannot be divided by {operand2}")
    except ValueError:
        pass
    except IndexError:
        pass

