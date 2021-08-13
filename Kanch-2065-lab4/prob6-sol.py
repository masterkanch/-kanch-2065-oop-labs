"""
Kanch Ruansiripiyakul 633040206-5

Program that calculate the sum of the list
"""


def sum_of_list(numbers):
    return sum(numbers)


def average(sum, n):
    try:  # ZeroDivisionError if list is empty
        return sum / n
    except ZeroDivisionError:
        pass


def final_data(data):
    for item in data:
        if len(item) == 0:
            print("The list is empty")
        else:
            print("Average:", average(sum_of_list(item), len(item)))


list1 = [10, 20, 30, 40, 50]
list2 = [100, 200, 300, 400, 500]
# empty list
list3 = []
lists = [list1, list2, list3]
final_data(lists)
