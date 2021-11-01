from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()


def coffee_machine():
    machine_running = True
    while machine_running:
        user_choice = input(f"What would you like? ({my_menu.get_items()}): ")
        if user_choice == "report":
            my_coffee_maker.report()
            my_money_machine.report()
        elif user_choice == "off":
            machine_running = False
        elif my_coffee_maker.is_resource_sufficient(my_menu.find_drink(user_choice)):
            if my_money_machine.make_payment(my_menu.find_drink(user_choice).cost):
                my_coffee_maker.make_coffee(my_menu.find_drink(user_choice))


coffee_machine()
