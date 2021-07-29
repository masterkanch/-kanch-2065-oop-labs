"""
Kanch Ruansiripiyakul 633040206-5

Program that add a number into a list, find and replace a number
in a list, and find and remove numbers in a list
"""


def add_number_to_list():
    global my_list
    print(f"Before adding an integer, the list is {my_list}")
    number = int(input("Enter a number to add to a list:"))
    my_list.append(number)
    print(f"After adding an integer {number}, the list is {my_list}")


def replace_number_in_list():
    global my_list
    print(f"Finding a number to replace in the list is {my_list}")
    index = int(input("Enter a number to find:"))
    number = int(input("Enter a new number to replace: "))
    my_list = [number if x == index else x for x in my_list]
    print(f"After replacing {index} with {number}, the new list is {my_list}")


def remove_number_from_list():
    global my_list
    print(f"Finding a number to remove in the list is {my_list}")
    number = int(input("Enter a number to remove:"))
    my_list.remove(number)
    print(f"After removing {number}, the list is {my_list}")


my_list = [1, 2, 3, 4, 5]
add_number_to_list()
replace_number_in_list()
remove_number_from_list()
