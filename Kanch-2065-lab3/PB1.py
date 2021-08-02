import random

if __name__ == "__main__":
    answer = random.randint(1, 10)
    guess_chance = 5
    while True:
        try:
            guess = int(input("Enter an integer to guess: "))
            if guess == answer:
                print("Congrats that you guess the number correctly!")
                break
            elif guess > answer and 10 > guess > 1:
                print("Try a lower number")
                guess_chance -= 1
                print(f"You have {guess_chance} guesses remaining")
                if guess_chance == 0:
                    break
                continue
            elif guess < answer and 10 > guess > 1:
                print("Try a higher number")
                guess_chance -= 1
                print(f"You have {guess_chance} guesses remaining")
                if guess_chance == 0:
                    break
                continue
            elif guess < 1 or guess > 10:
                print("Please guess with with an integer in the range [1,10]")
        except ValueError:
            print('Please enter an integer to guess')
