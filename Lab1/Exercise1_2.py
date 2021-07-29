while True:
    try:
        temp_cel = float(input("Enter a temperature in celsius: "))
        temp_fah = (9/5) * temp_cel + 32
        print(f"{round(temp_cel,2)} in Celsius is {round(temp_fah,2)}")
        break
    except ValueError:
         print("Please enter a valid floating point for temperature.")
    