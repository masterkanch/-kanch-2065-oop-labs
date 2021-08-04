import functools
def power_two_number(num):
    return num ** 2

def append_integer_list():
    for i in range(1,integer+1):
                integer_list.append(i)

if __name__ == "__main__":
    integer_list = []
    while True:
        try:
            integer = int(input("Enter an integer:"))
            append_integer_list()
            sum_of_square_list = functools.reduce(lambda a, b: a + b, list(map(power_two_number,integer_list)))
            print(f"The sum of the square of {integer_list} is {sum_of_square_list}")
            break
        except ValueError:
            print("Please enter an integer")