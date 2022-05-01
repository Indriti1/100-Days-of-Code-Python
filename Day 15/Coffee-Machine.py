from menu import MENU, resources

PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25


def print_report(money):
    """Prints a report of resources and the money that is currently on the machine."""
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${money}')


def check_resources_sufficient(choice_item):
    """Checks if the resources needed to make the order are sufficient and returns True/False based on the check."""
    item = MENU[choice_item]
    ingredients = item["ingredients"]
    for ingredient in ingredients:
        if ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    """Prompts the user to insert quarters, dimes, nickels and pennies and returns the total amount."""
    print("Please insert coins.")
    quarters_count = int(input("How many quarters?: "))
    dimes_count = int(input("How many dimes?: "))
    nickels_count = int(input("How many nickels?: "))
    pennies_count = int(input("How many pennies?: "))
    total = (quarters_count * QUARTER) + (dimes_count * DIME) + (nickels_count * NICKEL) + (pennies_count * PENNY)
    return total


def check_transaction_successful(total, choice_item):
    """Checks if the amount inserted for the item is enough and returns True/False and a message or a change."""
    item_price = MENU[choice_item]["cost"]
    if total < item_price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total == item_price:
        return True
    else:
        change = total - item_price
        print(f"Here is ${round(change, 2)} dollars in change.")
        return True


def process_order(choice_item):
    """Processes the user order and returns the payment"""
    item = MENU[choice_item]
    ingredients = item["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] = resources[ingredient] - ingredients[ingredient]
    payment = item["cost"]
    print(f"Here is your {choice_item} ☕ Enjoy!")
    return payment


def coffee_machine():
    """Starts the coffee machine program"""
    machine_on = True
    money = 0
    while machine_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "report":
            print_report(money)
        elif choice == "off":
            machine_on = False
        else:
            resources_checked = check_resources_sufficient(choice)
            if resources_checked:
                coins_inserted = process_coins()
                transaction_checked = check_transaction_successful(coins_inserted, choice)
                if transaction_checked:
                    payment = process_order(choice)
                    money = money + payment


coffee_machine()
