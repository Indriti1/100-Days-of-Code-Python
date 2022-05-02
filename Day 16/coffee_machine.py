from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True
while machine_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        machine_on = False
    else:
        menu_item = menu.find_drink(choice)
        if menu_item is not None:
            resources_checked = coffee_maker.is_resource_sufficient(menu_item)
            if resources_checked:
                payment_checked = money_machine.make_payment(menu_item.cost)
                if payment_checked:
                    coffee_maker.make_coffee(menu_item)
