import random


class PlayingWord:
    def __init__(self, word):
        self.word = list(word)

    def __str__(self):
        return " ".join(self.word)

    def __eq__(self, other):
        result = zip(self.word, other.word)
        all_correct = 1
        for tup in result:
            a, b = tup
            all_correct *= 1 if a == b else 0
        return bool(all_correct)

    def check_letters(self, guess):
        result_right_place = ""
        result_in_word = ""
        for i in range(5):
            if self.word[i] == guess.word[i]:
                result_right_place += self.word[i]
            else:
                result_right_place += "_"
        for letter in guess.word:
            if letter in self.word:
                letter_count = self.word.count(letter)
                result_in_word += (str(letter_count) + "x" + letter)
        return PlayingWord(result_right_place), result_in_word


words = ["KRZEM", "RUBIN", "BIEDA", "ANIOŁ"]

word = random.choice(words)
wrongs = 5
rounds = 1
guessing_word = PlayingWord(word)

while wrongs != 0 and rounds != 10:
    guess = PlayingWord(input("Guess word:"))
    if guess == guessing_word:
        print("_______________You won!! Grats!_______________")
        print(guessing_word)
        wrongs = 0
    else:
        print_tup = guessing_word.check_letters(guess)
        print(print_tup[0], print_tup[1])
    rounds += 1
