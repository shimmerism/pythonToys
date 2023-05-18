# Guess the Number Game v1.0
# Import libraries.
#import math
import random

# Welcome message.
print('----------------------------------------') 
print('Welcome to guess the number! Version 1.0')
print('----------------------------------------')


def startGame():
    # Number to be guessed.
    # Generates the random number.
    possibleNumbers = [1, 2, 3, 4, 5]
    number = random.choice(possibleNumbers)
    # Guess variable
    guess = int(input("Guess the Number from 1 to 5: "))
    # Checks if guess is correct.
    if guess == number:
        print("Correct!")
        # Prompts user for restart.
        restart = input("Do you want to try again? " )
        # Checks if restart was requested.
        if restart == "yes" or restart == "y":
            startGame()
        # Checks if restart was rejected.
        elif restart == "no" or restart == "n":
            exit()

        else:
            print("Error! command not found.")
            exit()
    else:
        print("Wrong!")
         # Prompts user for restart.
        restart = input("Do you want to try again? ")
        # Checks if restart was requested.
        if restart == "yes" or restart == "y":
            print("--------------------------")
            startGame()
        # Checks if restart was rejected.
        elif restart == "no" or restart == "n":
            print("--------------------------")
            exit()

        else:
            print("Error! command not found.")
            print("--------------------------")
            exit()

# Starts 
startGame()

