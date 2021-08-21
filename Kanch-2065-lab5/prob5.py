"""
Kanch Ruansiripiyakul 633040206-5

Calculator program
"""
ADD = 'add'
DIV = 'div'
MUL = 'mul'


def flexible_calculator(operator, output_format, *number):
    if operator == 'add':
        try:
            sum_num = 0
            if len(number) == 1:
                for num in number:
                    return num
            for num in number:
                sum_num = sum_num + num
            if output_format == 'float':
                return float(sum_num)
            elif output_format == 'int':
                return int(sum_num)
        except TypeError:
            pass
    elif operator == 'mul':
        mul_num = 1
        for num in number:
            mul_num = mul_num * num
        if output_format == 'float':
            return float(mul_num)
        elif output_format == 'int':
            return int(mul_num)
    elif operator == 'div':
        try:
            div_num = 0
            for num in number:
                div_num = num / num
            if output_format == 'float':
                return float(div_num)
            elif output_format == 'int':
                return int(div_num)
        except ZeroDivisionError:
            return "Cannot divide by zero"


if __name__ == '__main__':
    print(f"flexible_calculator(ADD,int,1) = {flexible_calculator(ADD, 'int', 1)}")
    print(f"flexible_calculator(ADD, 'int', 1, 2) = {flexible_calculator(ADD, 'int', 1, 2)}")
    print(f"flexible_calculator(ADD, 'int', 1, 2, 3, 4) = {flexible_calculator(ADD, 'int', 1, 2, 3, 4)}")
    print(f"flexible_calculator(MUL, 'int', 2, 3, 4) = {flexible_calculator(MUL, 'int', 2, 3, 4)}")
    print(f"flexible_calculator(DIV, 'float', 10, 5, 2) = {flexible_calculator(DIV, 'float', 10, 5, 2)}")
    print(f"flexible_calculator(DIV, 'float', 5, 0) = {flexible_calculator(DIV, 'float', 5, 0)}")
