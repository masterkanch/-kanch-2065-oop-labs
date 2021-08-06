import random

if __name__ == "__main__":
    ANSWER = random.randint(1, 10)
    GUESSES_CHANCE = 5
    while True:
        try:
            guess = int(input("Enter an integer to guess: "))
            if guess == ANSWER:
                print("Congrats that you guess the number correctly!")
                break
            elif guess > ANSWER and 10 > guess >= 1:
                print("Try a lower number")
                GUESSES_CHANCE -= 1
                if GUESSES_CHANCE == 0:
                    print("I am 0")
                    print(f"You have {GUESSES_CHANCE} guess remaining")
                    break
                elif GUESSES_CHANCE < 2:
                    print(f"You have {GUESSES_CHANCE} guess remaining")
                else:
                    print(f"You have {GUESSES_CHANCE} guesses remaining")
            elif guess < ANSWER and 10 > guess >= 1:
                print("Try a higher number")
                GUESSES_CHANCE -= 1
                if GUESSES_CHANCE == 0:
                    print(f"You have {GUESSES_CHANCE} guess remaining")
                    break
                elif GUESSES_CHANCE < 2:
                    print(f"You have {GUESSES_CHANCE} guess remaining")
                else:
                    print(f"You have {GUESSES_CHANCE} guesses remaining")
            elif guess < 1 or guess > 10:
                print("Please guess with with an integer in the range [1,10]")
        except ValueError:
            print('Please enter an integer to guess')
