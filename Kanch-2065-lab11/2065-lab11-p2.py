import re


def split_str(lst):
    for i in lst:
        word_list = re.split(r"\s", i)
        print(
            f"{word_list[0]} has email as {word_list[1]} and phone as {word_list[2]}")


if __name__ == '__main__':
    lst = ["mana mana@kku.ac.th 043-222-3333",
           "manee manee@kku.ac.th. 043-888-9999"]
    split_str(lst)
