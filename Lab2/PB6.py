"""
Kanch Ruansiripiyakul 633040206-5

Program that split a string
"""
olympics2020_str = "Badminton: Thailand vs. Great Britain,Table Tennis: Thailand vs. Japan"

if __name__ == "__main__":
    Split_strings = olympics2020_str.split(',')
    Badminton = Split_strings[0].split(':')
    Tabletennis = Split_strings[1].split(':')
    print("For some Olympics 2020 games of Thai athletes:")
    print(f"For {Badminton[0]}, the game is between {Badminton[1]}")
    print(f"For {Tabletennis[0]}, the game is between {Tabletennis[1]}")
