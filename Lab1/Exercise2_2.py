id = input("Please enter your student ID: ")
def Grade(score):
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

def Score(mt,fn):
    score = (0.4 * mt) + (0.6 * fn)
    return score

def Get_exam_mark(p):
    try: 
        midterm = float(input("Please enter the student's midterm exam mark (0-100): "))
        if  midterm >= 0.0 and midterm <= 100.0:
            return midterm
    except:
        print("Enter again")

while True:
    try:
        midterm = float(input("Please enter the student's midterm exam mark (0-100): "))
        if  midterm >= 0.0 and midterm <= 100.0:
            final = float(input("Please enter the student's final exam mark (0-100): "))
        if  final >= 0.0 and final <= 100.0:
            print(f"Student ID {id} has the total mark as {Score(midterm,final)} and has grade as {Grade(Score(midterm,final))}")
            break
    except:
        print("enter new score")
    
  