# 633040206-5 Kanch Ruansiripiyakul
def get_gpa():
    all_gpa_data = []
    while True:
        try:
            GPA = input("Enter GPA:")
            if GPA == 'q' or GPA == 'Q':
                return all_gpa_data
            GPA = float(GPA)
            if GPA >= 0 and GPA <= 4.0:
                all_gpa_data.append(GPA)
            elif GPA < 0 or GPA > 4.0:
                print("GPA must be in the range [0.0,4.0]")
                continue
        except ValueError:
            print("Please enter a valid GPA")


if __name__ == "__main__":
    print("Welcome to the program prob1.py by Kanch, 633040206-5 who has the average GPA as 1.96")
    name = input("Enter name:")
    all_gpa_data = get_gpa()
    average_gpa = sum(all_gpa_data) / len(all_gpa_data)
    print(f"{name} has average GPA as {average_gpa}")
    if average_gpa > 1.96:
        print(f"{name} has the average GPA greater than mine by {average_gpa - 1.96}")
    elif average_gpa < 1.96:
        print(f"{name} has the average GPA less than mine by {1.96 -average_gpa}")
    elif average_gpa == 1.96:
        print(f"{name} has the average the same as mine.{1.96 -average_gpa}")
