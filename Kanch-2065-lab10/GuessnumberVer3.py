from GuessnumberVer2 import GuessNumberGameVer2
"""
Kanch Ruansiripiyakul 633040206-5
"""


class GuessNumberGameVer3(GuessNumberGameVer2):
    def __init__(self, *args, **kwargs):
        super(GuessNumberGameVer3, self).__init__(*args, **kwargs)

    # overriding playgames function from GuessNumberVer2 for ask more answer
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
            elif answer == 'v':
                self.guessAveraged()
                continue
            elif answer == 'm':
                self.guessMin()
                continue
            elif answer == 'x':
                self.guessMax()
                continue
            else:
                continue

    # override method from GuessNumberGameVer2 for adding more feature for user
    def promtGamemsg(self):
        answer = input(
            "If you want to play again? type 'y' to continue or 'q' to quit.\nType 'a' to see all your guessses or 'g' to see a guess on specific play\nType 'v' to see average or 'm' to see minimum or 'x' to see maximum of all your guesses.\n")
        return answer

    # print the average answer that user guesses
    def guessAveraged(self):
        print(f"Average = {round(sum(self._guess) / len(self._guess),2)}")

    # print the minimum number of answer that user guesses
    def guessMin(self):
        print(f"Min = {min(self._guess)}")

    # print the maximum number of answer that user guesses
    def guessMax(self):
        print(f"Max = {max(self._guess)}")


if __name__ == '__main__':
    gng1 = GuessNumberGameVer3(5, 8, 4)
    print(gng1)
    gng1.playGames()
