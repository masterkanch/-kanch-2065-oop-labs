from random import randint
"""
Kanch Ruansiripiyakul 633040206-5
"""


class GuessNumberGameVer1:
    _numOfGames = 0

    def __init__(self, minnum=1, maxnum=10, maxTries=3):
        # use for count the number of the object that are create
        GuessNumberGameVer1._numOfGames += 1
        self._minnum = minnum
        self._maxnum = maxnum
        self._maxTries = maxTries

    # return the string representation of the object
    def __str__(self):
        return f"Guess number game:({self._minnum}, {self._maxnum}, {self._maxTries})"

    # return the number of the object that are create
    @classmethod
    def getNumofGames(self):
        return self._numOfGames

    # function that play game
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


if __name__ == "__main__":
    gng1 = GuessNumberGameVer1()
    gng2 = GuessNumberGameVer1(5, 8)
    gng3 = GuessNumberGameVer1(5, 8, 4)
    print(gng3)
    print(
        f"The current number of game is {GuessNumberGameVer1.getNumofGames()}")
    gng3.playGame()
