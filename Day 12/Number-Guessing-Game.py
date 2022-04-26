from art import logo
from random import randint

EASY_DIFFICULTY_TRIES = 10
HARD_DIFFICULTY_TRIES = 5


def check_answer(choice, number, tries):
    """Checks the if the user choice is equal to the randomly guessed number, prints the correct message and if not equal reduces the number of tries"""
    if choice < number:
        print('Too low.')
        return tries - 1
    elif choice > number:
        print('Too high.')
        return tries - 1
    elif choice == number:
        print(f'You got it! The answer was {choice}.')
        return tries


def set_difficulty():
    """Takes a user input for difficulty and sets the number of tries"""
    difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
    if difficulty == 'easy':
        tries = EASY_DIFFICULTY_TRIES
    elif difficulty == 'hard':
        tries = HARD_DIFFICULTY_TRIES
    return tries


def game():
    """Starts the number guessing game"""
    number = randint(1, 100)
    print('Welcome to the Number Guessing Game!')
    print('I\'m thinking of a number between 1 and 100.')

    choice = 0
    tries = set_difficulty()
    while choice != number:
        print(f'You have {tries} attempts remaining to guess the number.')
        choice = int(input('Make a guess: '))
        tries = check_answer(choice, number, tries)
        if tries > 0:
            print('Guess again.')
        else:
            print('You have run out of guesses, you lose.')


print(logo)
game()