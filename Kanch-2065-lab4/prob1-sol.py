"""
Kanch Ruansiripiyakul 633040206-5

Program that caluculate bmi
"""
patients = [[70, 1.80], [58, 1.55], [150, 1.70]]


def calculate_bmi(_weight, _height):
    return (_weight / (_height ** 2))


for i, values in enumerate(patients):
    weight, height = values
    bmi = calculate_bmi(weight, height)
    print(f"Patient's BMI is: {bmi:0.02f}")
