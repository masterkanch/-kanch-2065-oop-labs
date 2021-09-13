# 633040206-5 Kanch Ruansiripiyakul

def print_welcome_msg(NAME, ID, HOMETOWN):
    print(
        f"Welcome to the program prob2.py by {NAME}, {ID} who has hometown as {HOMETOWN}")


def read_file():
    with open("mycourses.txt", "r") as mycourses:
        contents = mycourses.read()
        return contents


def init_course_info(data):
    all_data = {}
    data = data.replace('"', '')
    data = data.replace(':', '')
    data = data.replace('{', '')
    data = data.replace('}', '')
    all_data[data[1:5]] = data[7:43]
    return all_data


def update_course_info(mycourses, year, *data):
    if year == "2563":
        mycourses['2563'] = data
    elif year != "2563":
        mycourses[year] = data


def write_file(mycourses):
    with open("mycourses.txt", "w") as courses:
        courses.write(mycourses)


if __name__ == "__main__":
    print_welcome_msg("Kanch", "633040206-5", "Nakhon panom")
    data = read_file()
    my_courses = init_course_info(data)
    update_course_info(my_courses, "2563",
                       "English for Comminication in Multicultural Societies")
    update_course_info(my_courses, "2563",
                       "EnglishCritical Reading and writing")
    print(my_courses)
    write_file(my_courses)
