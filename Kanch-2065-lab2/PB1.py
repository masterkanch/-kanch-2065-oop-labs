"""
Kanch Ruansiripiyakul 633040206-5

Program that convert a distance given in degrees
Celsius to its equivalent in degrees Fahrenheit
"""
while True:
    try:
        Temp_cel = round(float(input("Enter a temperature in Celsius: ")), 2)
        Temp_fah = round((9 / 5) * Temp_cel + 32, 2)
        print(f"{Temp_cel} in Celsius is {Temp_fah}")
        break
    except ValueError:
        print("Please enter a valid floating point for the temperature.")
