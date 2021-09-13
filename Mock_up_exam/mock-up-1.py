def add_emails():
    email_course = {}
    while True:
        email = input("Enter an email address: ")
        if email == "q" or email == "Q":
            break
        course = input("Enter a course: ")
        # add key value to email_course = {} dictionary
        email_course.setdefault(email, course)
    if email_course:  # if email_course have some data
        return email_course  # return dictionary
    else:
        return None


def get_course_info(email_course, req_course):
    emails = []
    for email, course in email_course.items():  # .items = return each pair of email_course
        if course == req_course:
            # appens email to emails that corresponding to req_course
            emails.append(email)
    return emails


def print_course_info(email_course):
    # email_course.values() = 842004, 842005, 842004
    courses = set(email_course.values())
    # chang value to set bc it will have no duplicate num.
    # if email register to the same course, it will match to the same group
    for course in courses:
        emails = get_course_info(email_course, course)
        num_students = len(emails)
        if num_students == 1:
            print(f" {num_students} is registered")
        else:
            print(f" {num_students} are are registered")
        print(f"For course {course}, {num_students} ")
        print(f"These students have emails {emails}")


def print_email_info(email_course):
    if email_course is not None:
        print(email_course)


if __name__ == "_main_":
    email_course = add_emails()
    print_email_info(email_course)
    print_course_info(email_course)
