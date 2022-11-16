#!/usr/bin/env python3

# Created by: Tamer Zreg
# Date: Nov.8, 2022
# This program checks if the user guessed a number correctly
# using a do-while loop

# Imports secret number
import constants


def main():

    # 'Do while loop' that repeats until user enters
    # a correct guess.
    while True:

        # Gets the user's guess
        user_guess_str = input("Enter a number from 0 to 9: ")

        # Tries casting the user's guess to an integer
        try:
            user_guess_int = int(user_guess_str)

        # Restarts if the user did not enter a number
        except ValueError:
            print("You must enter a number.")
            return main()

        # Breaks loop if the user guessed correctly
        if user_guess_int == constants.SECRET_NUMBER:
            break

        print("Incorrect.\n\n")

    # Tells the user they are correct
    print("Correct!")


if __name__ == "__main__":
    main()
