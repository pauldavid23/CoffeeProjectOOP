from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

the_menu = Menu()
infinite_loop = True

while infinite_loop is True:
    options = the_menu.get_items()
    selection = input(f"What do you like to order: {options}")

    if selection == "off":
        print("Goodbye!")
        infinite_loop = False
    elif selection == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        the_drink = the_menu.find_drink(selection)
        if coffee_maker.is_resource_sufficient(the_drink) and money_machine.make_payment(the_drink.cost):
            coffee_maker.make_coffee(the_drink)
        else:
            print("Insufficient resources!")

