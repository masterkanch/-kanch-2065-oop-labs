import functools


def filter_positive_odd_num(num):
    if num > 0 and num % 2 != 0:
        return True
    else:
        return False


def compute_sum_positive_odd_numbers():
    while True:
        try:
            numbers_list = list(map(int, input("Enter numbers in the list:").split()))
            numbers_list = list(filter(filter_positive_odd_num, numbers_list))
            print(functools.reduce(lambda a, b: a + b, numbers_list))
            break
        except ValueError:
            print("Please enter number")


if __name__ == "__main__":
    compute_sum_positive_odd_numbers()
