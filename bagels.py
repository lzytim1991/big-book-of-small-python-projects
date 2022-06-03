import random

intro = """
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:     That means:
    Pico        One digit is correct but in the wrong position
    Fermi       One digit is correct and in the right position
    Bagels      No digit is correct.

I have thought of a number.
    You have 10 guesses to get it.
"""

answer = str(random.randint(100, 1000))


def get_user_input(tries):
    # gets an input from the user

    message = f'Guess {tries}: '
    return input(message)
