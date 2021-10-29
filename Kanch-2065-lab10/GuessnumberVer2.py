from GuessnumberVer1 import GuessNumberGameVer1
from random import randint
"""
Kanch Ruansiripiyakul 633040206-5
"""


class GuessNumberGameVer2(GuessNumberGameVer1):
    def __init__(self, *args, **kwargs):
        super(GuessNumberGameVer2, self).__init__(*args, **kwargs)
        self._guess = []
        self._numGuesses = 0

    def playGame(self):
        # random answer
        answer = randint(self._minnum, self._maxnum)
        print(
            f"GuessNumberGame with min number as {self._minnum}, max number as {self._maxnum}, max num of tries as {self._maxTries}")
        guess = input(
            f"Please enter a guess ({self._minnum}, {self._maxnum}):")
        # append guess answer to an array
        self._guess.append(int(guess))

        numTries = self._maxTries
        # checking for the number of wrong guess
        while numTries > 0:
            numTries = numTries - 1
            if numTries == 0:
                print("Wrong please try again later")
                break
            if int(guess) == answer:
                print(f"Congratulations! That's correct")
                break
            elif int(guess) < answer:
                print(
                    f"Please type a higher number! The number of remaining tries is {numTries}")
            else:
                print(
                    f"Please type a lower number! The number of remaining tries is {numTries}")
            guess = input(
                f"Please enter a guess ({self._minnum}, {self._maxnum}):")
            self._guess.append(int(guess))

    def playGames(self):
        # using playgame function from GuessNumberGameVer1
        self.playGame()
        # When the game end the program will promt the user for what to doing next
        while True:
            answer = self.promtGamemsg()
            if answer == 'q':
                break
            elif answer == 'y':
                self.playGame()
            elif answer == 'a':
                self.showGuesses()
                continue
            elif answer == 'g':
                self.showSpecific()
                continue
            else:
                continue

    # ask user for what to doing next
    def promtGamemsg(self):
        answer = input(
            "If you want to play again? type 'y' to continue or 'q' to quit.\nType 'a' to see all your guessses or 'g' to see a guess on specific play:")
        return answer

    # show the answer that user have ask in the game
    def showGuesses(self):
        print(self._guess)

    # show the specific answer that user have ask in the game
    def showSpecific(self):
        if len(self._guess) == 1:
            while True:
                try:
                    guess_index = int(
                        input("Enter which guess in in the range [1]:"))
                    if guess_index == 1:
                        print(self._guess[guess_index-1])
                        break
                    else:
                        continue
                except ValueError:
                    continue
        elif len(self._guess) > 1:
            while True:
                try:
                    guess_index = int(input(
                        f"Enter which guess is in the range [1, {len(self._guess)}]:"))
                    if guess_index in range(1, len(self._guess)+1):
                        print(self._guess[guess_index-1])
                        break
                    else:
                        continue
                except ValueError:
                    continue


if __name__ == '__main__':
    gng1 = GuessNumberGameVer2(5, 8, 4)
    print(gng1)
    gng1.playGames()
