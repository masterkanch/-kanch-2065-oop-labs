# 633040206-5 Kanch ruansiripiyakul

import json
student_data = {}


def add_emails():
    student_data = {}
    while True:
        try:
            email = input(f"Enter an email address:")
            if email == 'q' or email == 'Q':
                return student_data
            course = input(f"Enter a course:")
            student_data[email] = course
        except ValueError:
            pass


def print_emails_info():
    with open('students.json', 'r') as student_json:
        data = json.load(student_json)
        print(data)


def write_json_data(student_data):
    with open('students.json', 'w') as student_json:
        json.dump(student_data, student_json)


def print_corse_info():
    with open('students.json', 'r') as student_json:
        data = json.load(student_json)
        for i in data:
            print(f'{i} registered for course {data[i]}')


if __name__ == "__main__":
    student_data = add_emails()
    write_json_data(student_data)
    print_emails_info()
    print("=== Writing emails and courses to file students.json ===")
    print("=== Reading emails and courses from file students.json ===")
    print_corse_info()
