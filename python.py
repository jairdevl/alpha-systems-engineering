import random

def main():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    print("Try to guess the number in as few attempts as possible.\n")

    number = random.randint(1, 100)
    attempts = 0
    guess = 0

    while guess != number:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
        else:
            print("Congratulations! You guessed the number in", attempts, "attempts.")