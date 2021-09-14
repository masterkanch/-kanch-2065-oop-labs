"""
Kanch Ruansiripiyakul 633040206-5
"""


class Teacher:
    def __init__(self, name, office, research_topic, *courses):
        self.name = name
        self.office = office
        self.research_work = research_topic
        self.course_work = courses

    def print_office_no(self):
        print(f"{self.name} has the office at {self.office}")

    def print_research_work(self):
        print(f"{self.name} is doing research in these topics {self.research_work}")

    def print_courses_work(self):
        print(f"{self.name} teaches these courses {self.course_work}")


if __name__ == "__main__":
    manee = Teacher("Manee", "Rm. 4203",
                    "Artificial Intelligence", "EN842004", "EN813701")
    mana = Teacher("Mana", "Rm. 4209", "Internet of Things",
                   "EN842005", "EN813703")
    manee.print_office_no()
    manee.print_research_work()
    manee.print_courses_work()
    mana.print_office_no()
    mana.print_research_work()
    mana.print_courses_work()
