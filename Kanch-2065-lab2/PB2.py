"""
Kanch Ruansiripiyakul 633040206-5

Program that 
assign grades to students at the end of the year
"""
def grading(score):
    if score < 50.0:
        return "F"
    elif score >= 50.0 and score < 60.0:
        return "D"
    elif score >= 60.0 and score < 70.0:
        return "C"
    elif score >= 70.0 and score < 80.0:
        return "B"
    elif score >= 80.0 and score <= 100.0:
        return "A"


def calculate_Score(mt, fn):
    score = (0.4 * mt) + (0.6 * fn)
    return score


def get_exam_mark(p):
    while True:
        try:
            Score = float(input(f"Please enter the student's {p} exam mark (0-100): "))
            return Score
        except ValueError:
            print("Enter a score as a decimal number")
            continue


id = input("Please enter your student ID: ")
Midterm_score = get_exam_mark("midterm")
Final_score = get_exam_mark("final")
Total_score = calculate_Score(Midterm_score, Final_score)
Grade = grading(Total_score)
print(f"Student ID {id} has the total mark as {Total_score} and has grade as {Grade}")
