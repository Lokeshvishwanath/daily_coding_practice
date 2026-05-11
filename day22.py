# Day 22 - Number Guessing Game

import random

class NumberGuessingGame:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

    def play(self):
        print("=== Number Guessing Game ===")
        print("Guess a number between 1 and 100\n")

        while True:
            guess = int(input("Enter your guess: "))
            self.attempts += 1

            if guess < self.secret_number:
                print("Too low! Try again.\n")

            elif guess > self.secret_number:
                print("Too high! Try again.\n")

            else:
                print(f"\nCorrect! The number was {self.secret_number}")
                print(f"You guessed it in {self.attempts} attempts.")
                break


def main():
    game = NumberGuessingGame()
    game.play()


if __name__ == "__main__":
    main()