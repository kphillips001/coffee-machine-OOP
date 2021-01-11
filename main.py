from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Print Report
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

coffee_maker.report()
money_machine.report()

while is_on:
  options = menu.get_items()
  choice = input(f"What would you like? {options}: ")
  if choice == "off":
    is_on = False
  elif choice == "report":
    coffee_maker.report()
    money_machine.report()
  else:
    drink = menu.find_drink(choice)
    # Check sufficient resources
    is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
    # Process coins & check transaction successful
    is_payment_successful = money_machine.make_payment(drink.cost)
    if is_enough_ingredients and is_payment_successful:  
      # Make coffee
      coffee_maker.make_coffee(drink)

    
