"""
Kanch Ruansiripiyakul 633040206-5

Program that calculate average of input number
"""
sum = 0
count = 0
end_input = False
while not end_input:
    try:
        n = int(input("Enter an integer:"))
        if n < 0:
            print(f"Average is {avg}")
            end_input = True
        sum = sum + n
        count = count + 1
        avg = sum / count
    except ValueError:
        print("Please enter a valid integer")
        break
