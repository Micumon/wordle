import random


class PlayingWord:
    def __init__(self, word):
        self.word = list(word)

    def __str__(self):
        return " ".join(self.word)


words = ["KRZEM", "RUBIN", "BIEDA", "ANIOŁ"]

word = random.choice(words)
wrongs = 5
rounds = 1
guesing_word = PlayingWord(word)

while wrongs != 0 and rounds != 10:
    guess = input("Guess word:")

