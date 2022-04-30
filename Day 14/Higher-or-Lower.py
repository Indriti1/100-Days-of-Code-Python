from art import logo, vs
import random
from game_data import data
from replit import clear

first_user = ""
second_user = ""


def random_user():
    '''Gets a random user from the list of users'''
    user = random.choice(data)
    return user


def compare_users(first_user, second_user, choice):
    '''Compares users follower numbers and the user choice and check if user is correct'''
    user_1_followers = first_user["follower_count"]
    user_2_followers = second_user["follower_count"]

    if user_1_followers >= user_2_followers and choice == 'a':
        return True
    elif user_1_followers < user_2_followers and choice == 'a':
        return False
    elif user_1_followers >= user_2_followers and choice == 'b':
        return False
    elif user_1_followers < user_2_followers and choice == 'b':
        return True


def user_information(user):
    '''Returns a formatted information about the user'''
    name = user["name"]
    description = user["description"]
    country = user["country"]
    return f"{name}, a {description}, from {country}."


def prompt(first_user, second_user):
    '''Prints a formatted terminal with users inputted and asks user for a choice'''
    print(f"Compare A: {user_information(first_user)}")
    print(f"{vs}")
    print(f"Against B: {user_information(second_user)}")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    return choice


def choose_and_check(first_user, second_user):
    '''Gets users and returns their comparison'''
    choice = prompt(first_user, second_user)
    check = compare_users(first_user, second_user, choice)
    return check


def clear_and_reprint():
    '''Clears the terminal and reprints the logo'''
    clear()
    print(logo)


def higher_or_lower():
    '''Starts a new higher or lower game'''
    print(logo)
    game_over = False;
    count = 0
    second_user = random_user()

    while not game_over:
        first_user = second_user
        second_user = random_user()
        if first_user == second_user:
            second_user = random_user()

        check = choose_and_check(first_user, second_user)
        clear_and_reprint()
        if check:
            count += 1
            print(f"You're right! Current score: {count}")
        else:
            game_over = True
            print(f"Sorry that's wrong. Final score: {count}")

higher_or_lower()