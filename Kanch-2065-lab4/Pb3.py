def get_infected_cases(p):
    while True:
        try:
            new_infected_cases = int(
                input(f'Enter the number of new infected Covid19 cases for {p}:'))
            if new_infected_cases >= 0:
                print("Stay healthy!")
                return new_infected_cases
            elif new_infected_cases < 0:
                print("You can only enter a non-negative integer")
                print("Stay healthy!")
        except ValueError:
            print("Please enter a valid integer")
            print("Stay healthy!")


def compute_percent(today_cases, yesterday_cases):
    difference = abs(today_cases - yesterday_cases)
    percent = float((difference / yesterday_cases) * 100)
    return percent


def main():
    yesterday_cases = get_infected_cases("yesterday")
    today_cases = get_infected_cases("today")
    percent = compute_percent(today_cases, yesterday_cases)
    print(f"The difference of the number of new infected cases is {percent}%")


if __name__ == "__main__":
    main()
